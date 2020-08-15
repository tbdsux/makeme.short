from flask import render_template, request, Blueprint, flash, url_for, redirect, jsonify, make_response
from flask_login import login_user, current_user, logout_user, login_required
from sqlalchemy import func, desc, and_
from makemeshort import db
from makemeshort.models import ShortenedLinks, Clicks
from makemeshort.links.forms import ShortenLinkForm, DeleteLinkForm, UpdateLinkDescriptionForm
import geocoder  # for getting the location from the ip
from werkzeug.urls import url_parse
import requests

links = Blueprint('links', __name__)


@links.context_processor
def get_country_processor():
    def get_country(alphacode):
        if alphacode is not None:
            r = requests.get('https://restcountries.eu/rest/v2/alpha/' +
                             alphacode + '?fields=name').json()
            return r['name']
        return None
    return dict(get_country=get_country)


@links.context_processor
def get_countryflag_processor():
    def get_countryflag(alphacode):
        if alphacode is not None:
            r = requests.get('https://restcountries.eu/rest/v2/alpha/' +
                             alphacode + '?fields=flag').json()
            return r['flag']
    return dict(get_countryflag=get_countryflag)


@links.route('/dashboard/links/<string:shorturl>')
@login_required
def stats_links(shorturl):
    form = ShortenLinkForm()
    deleteLinkForm = DeleteLinkForm()
    updateLinkDescForm = UpdateLinkDescriptionForm()

    shortlink = ShortenedLinks.query.filter_by(
        shorten_url=shorturl, author=current_user).first_or_404()

    if request.method == 'GET':
        updateLinkDescForm.description.data = shortlink.description

    clicks = Clicks.query.filter_by(link=shortlink).all()
    req_countries = db.session.query(Clicks.location, func.count(Clicks.id).label('cnt')).group_by(
        Clicks.location).filter(Clicks.link == shortlink, Clicks.shortlink_author == current_user, Clicks.location != None).order_by(desc('cnt')).limit(3).all()
    req_referrer = db.session.query(Clicks.referrer, func.count(Clicks.id).label('rcnt')).group_by(
        Clicks.referrer).filter(Clicks.link == shortlink, Clicks.shortlink_author == current_user).order_by(desc('rcnt')).limit(3).all()

    # for the chart
    cpd = db.session.query(func.date(Clicks.date_clicked), func.count(Clicks.id).label('count')).group_by(
        func.date(Clicks.date_clicked)).filter(Clicks.link == shortlink, Clicks.shortlink_author == current_user).order_by(func.date(Clicks.date_clicked)).all()

    __tempClicks = list(zip([x.strftime('%m/%d/%Y')
                             for x in (i[0] for i in cpd)], [i[1] for i in cpd]))

    shortlinkData = [list(i) for i in __tempClicks]
    return render_template('dashboard/stats.html', shortenForm=form, title='Overview - ' + shortlink.shorten_url, deleteLinkForm=deleteLinkForm, updateLinkDescForm=updateLinkDescForm, shortlinkData=shortlinkData, shortlink=shortlink, domain=request.url_root, clicks=clicks, top_countries=req_countries, top_referrer=req_referrer)


# shorten new link
@links.route('/dashboard/shorten/new', methods=['POST'])
@login_required
def shorten_link():
    form = ShortenLinkForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            # check if the long url already exists
            link = ShortenedLinks.query.filter_by(
                long_url=form.link.data).first()

            # if longurl doesnt exist
            if not link:
                # add data to database
                link = ShortenedLinks(
                    long_url=form.link.data, description=form.description.data, author=current_user)
                db.session.add(link)
                db.session.commit()

            return redirect(url_for('links.stats_links', shorturl=link.shorten_url))
        else:
            # if there is a problem in the validation, redirect to the referer
            return redirect(request.referer)


# redirect link
@links.route('/<string:shorturl>')
def redirect_link(shorturl):
    shortenedurl = ShortenedLinks.query.filter_by(
        shorten_url=shorturl).first_or_404()

    if shortenedurl:
        # do not add the crawler bots in the clicks (beta testing)
        if request.headers.get('Sec-Fetch-Site') and request.headers.get('Sec-Fetch-Mode') and request.headers.get('Sec-Fetch-Dest'):
            click = Clicks(client_ip=request.environ['HTTP_X_FORWARDED_FOR'], location=geocoder.ipinfo(request.environ['HTTP_X_FORWARDED_FOR']).country,
                           referrer=parse_url(request.referrer), link=shortenedurl, shortlink_author=shortenedurl.author)
            db.session.add(click)
            db.session.commit()

    return redirect(shortenedurl.long_url)


# delete link
@links.route('/dashboard/link/delete/<string:shorturl>', methods=['POST'])
def delete_link(shorturl):
    form = DeleteLinkForm()

    shortlink = ShortenedLinks.query.filter_by(
        shorten_url=shorturl, author=current_user).first_or_404()

    shortlinkClicks = Clicks.__table__.delete().where(
        and_(Clicks.link == shortlink, Clicks.shortlink_author == current_user))

    if shortlink.author != current_user:
        return redirect(url_for('users.links'))

    if request.method == 'POST':
        if form.validate_on_submit():
            db.session.execute(shortlinkClicks)
            db.session.delete(shortlink)
            db.session.commit()

            return redirect(url_for('users.links'))


# update link description
@links.route('/dashboard/link/description/edit/<string:shorturl>', methods=['POST'])
def edit_link_desc(shorturl):
    form = UpdateLinkDescriptionForm()

    shortlink = ShortenedLinks.query.filter_by(
        shorten_url=shorturl, author=current_user).first_or_404()

    if shortlink.author != current_user:
        return redirect(url_for('users.links'))

    if request.method == 'POST':
        if form.validate_on_submit():
            shortlink.description = form.description.data
            db.session.commit()
            return redirect(url_for('links.stats_links', shorturl=shortlink.shorten_url))


def parse_url(referer):
    if referer is not None:
        __ref = url_parse(referer).host
        # only get the host if it is not from the the same website
        if not __ref == url_parse(request.url_root).host:
            return __ref

    return 'Direct'
