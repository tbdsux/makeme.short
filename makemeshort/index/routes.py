from flask import render_template, request, Blueprint, flash, url_for, redirect, jsonify, make_response
from flask_login import current_user
from makemeshort import db
from makemeshort.models import QuickLinks
from makemeshort.links.forms import DirectShortenLinkForm

index = Blueprint('index', __name__)


@index.route('/')
def home():
    # bypass if user is currently authenticated
    if current_user.is_authenticated:
        return redirect(url_for('users.dashboard'))
        
    quickShortenForm = DirectShortenLinkForm()
    return render_template('index/home.html', quickShortenForm=quickShortenForm)


# quickly shorten urls
@index.route('/_quick-shorten/new', methods=['POST'])
def quick_shorten():
    req = request.get_json()

    # if the request is none
    if req['longurl'] is None:
        return redirect(url_for('index.home'))

    if request.method == 'POST':
        quicklink = QuickLinks(longurl=req['longurl'])

        try:
            db.session.add(quicklink)
            db.session.commit()
        except Exception:
            # when the data exists already
            quicklink = QuickLinks.query.filter_by(
                longurl=req['longurl']).first_or_404()

        res = make_response(
            jsonify({"shortlink": request.url_root + "q/" + quicklink.shortlink}), 200)

        return res


# redirect quick links
@index.route('/q/<string:quicklink>')
def quick_redirect(quicklink):
    getquickshort = QuickLinks.query.filter_by(
        shortlink=quicklink).first_or_404()

    if getquickshort:
        return redirect(getquickshort.longurl)
