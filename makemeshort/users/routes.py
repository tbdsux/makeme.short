from flask import render_template, request, Blueprint, flash, url_for, redirect, current_app, jsonify
from flask_login import login_user, current_user, logout_user, login_required
from sqlalchemy import func
from makemeshort import db, bcrypt
from makemeshort.models import User, ShortenedLinks, Clicks
from makemeshort.users.forms import LoginForm, RegisterForm, UpdateUserPassword, UpdateUserInfo, ForgotPassReqForm, EnterNewPassForm
from makemeshort.links.forms import ShortenLinkForm
from makemeshort.users.utils import save_profile_pic, send_reset_email
import os
import time

users = Blueprint('users', __name__)


@users.route('/datas')
def datas():
    links = ShortenedLinks.query.all()
    clicks = Clicks.query.all()
    return jsonify({links: clicks}), 200


@users.route('/account/login')
def login():
    loginForm = LoginForm()
    registerForm = RegisterForm()
    return render_template('forms/login_register.html', formtitle='Login', loginform=loginForm, registerform=registerForm)


@users.route('/account/login/continue', methods=['POST'])
def login_acc():
    # bypass if user is currently authenticated
    if current_user.is_authenticated:
        return redirect(url_for('users.dashboard'))

    loginForm = LoginForm()
    registerForm = RegisterForm()

    if request.method == 'POST':
        if loginForm.validate_on_submit():
            user = User.query.filter_by(
                username=loginForm.username.data).first()
            if user and bcrypt.check_password_hash(user.password, loginForm.password.data):
                login_user(user, remember=loginForm.remember.data)
                next_page = request.args.get('next')
                return redirect(url_for(next_page)) if next_page else redirect(url_for('users.dashboard'))
            else:
                flash('Incorrect Email / Password', 'red')
                return redirect(url_for('users.login'))

    return render_template('forms/login_register.html', formtitle='Login', loginform=loginForm, registerform=registerForm, display_login='block', display_register='hidden')


@users.route('/account/login/register', methods=['POST'])
def register_acc():
    # bypass if user is currently authenticated
    if current_user.is_authenticated:
        return redirect(url_for('users.dashboard'))

    loginForm = LoginForm()
    registerForm = RegisterForm()

    if request.method == 'POST':
        if 'agree' in request.form:
            if registerForm.validate_on_submit():
                hashed_pass = bcrypt.generate_password_hash(
                    registerForm.password.data).decode('utf-8')
                user = User(username=registerForm.username.data,
                            email=registerForm.email.data, password=hashed_pass)

                db.session.add(user)
                db.session.commit()
                login_user(user)

                return redirect(url_for('users.dashboard'))
        else:
            flash('Please accept the Terms and Agreement', 'blue')
            return redirect(url_for('users.login'))

    return render_template('forms/login_register.html', formtitle='Login', loginform=loginForm, registerform=registerForm, display_register='block', display_login='hidden')


# forgot password
@users.route('/account/forgot/password', methods=['GET', 'POST'])
def request_forgot_pass():
    # check if user is currently logged in
    if current_user.is_authenticated:
        return redirect(url_for('users.dashboard'))
    form = ForgotPassReqForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            send_reset_email(user)  # send the email
            flash('An email has been sent to your email address with instructions to reset your password.', 'blue')

    return render_template('forms/forgotpass.html', formtitle='Forgot Password', form=form)


# forgot password > enter new password
@users.route('/account/new/password/<token>', methods=['GET', 'POST'])
def request_new_pass(token):
    # check if user is currently logged in
    if current_user.is_authenticated:
        return redirect(url_for('users.dashboard'))

    form = EnterNewPassForm()

    user = User.verify_resetpass_token(token)

    if user is None:
        flash('Request password token is invalid or expired!', 'red')
        return redirect(url_for('users.request_forgot_pass'))

    if request.method == 'POST':
        hashed_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_pass
        db.session.commit()

        flash('Your password has been successfully updated!', 'green')
        return redirect(url_for('users.login'))


    return render_template('forms/newpass.html', formtitle='Reset Password', form=form)


# logout user
@users.route('/dashboard/account/logout')
def logout_acc():
    logout_user()
    return redirect(url_for('users.login'))


# dashboard
@users.route('/dashboard')
@login_required
def dashboard():
    clicksTotal = Clicks.query.filter_by(shortlink_author=current_user).count()
    linksTotal = ShortenedLinks.query.filter_by(author=current_user).count()

    # for the chart
    cpd = db.session.query(func.date(Clicks.date_clicked), func.count(Clicks.id).label('count')).group_by(
        func.date(Clicks.date_clicked)).filter(Clicks.shortlink_author == current_user).order_by(func.date(Clicks.date_clicked)).all()
    __tempClicks = list(zip([x.strftime('%m/%d/%Y')
                             for x in (i[0] for i in cpd)], [i[1] for i in cpd]))
    clicksData = [list(i) for i in __tempClicks]

    form = ShortenLinkForm()
    return render_template('dashboard/index.html', title='Dashboard', shortenForm=form, clicksData=clicksData, clicksTotal=clicksTotal, linksTotal=linksTotal)


# links
@users.route('/dashboard/links')
@login_required
def links():
    form = ShortenLinkForm()
    user_links = ShortenedLinks.query.filter_by(author=current_user).all()
    return render_template('dashboard/links.html', title='My Links', shortenForm=form, userlinks=user_links, domain=request.url_root)


# acc settings
@users.route('/dashboard/account', methods=['GET'])
@login_required
def account():
    form = ShortenLinkForm()
    formUpUser = UpdateUserInfo()
    formUpPass = UpdateUserPassword()

    if request.method == 'GET':
        formUpUser.username.data = current_user.username
        formUpUser.email.data = current_user.email

    return render_template('dashboard/acc_settings.html', title='Account Settings', currentUsername=current_user.username, currentEmail=current_user.email, shortenForm=form, formUpUser=formUpUser, formUpPass=formUpPass)


# update user info
@users.route('/dashboard/account/update/user', methods=['POST'])
def update_userinfo():
    form = ShortenLinkForm()
    formUpUser = UpdateUserInfo()
    formUpPass = UpdateUserPassword()

    if request.method == 'GET':
        formUpUser.username.data = current_user.username
        formUpUser.email.data = current_user.email

    if request.method == 'POST':
        if formUpUser.validate_on_submit():
            # check if the datas exist in order to update them...
            if formUpUser.profile_img.data:
                # delete the existing profile picture if not default
                if current_user.profile_img != 'default.jpg':
                    pimg_path = os.path.join(
                        current_app.root_path, 'static\\profile', current_user.profile_img)
                    try:
                        os.remove(pimg_path)
                    except FileNotFoundError:
                        pass

                # change the profile pic
                pic_file = save_profile_pic(formUpUser.profile_img.data)
                current_user.profile_img = pic_file

            if formUpUser.username.data:
                current_user.username = formUpUser.username.data  # update username
            if formUpUser.email.data:
                current_user.email = formUpUser.email.data  # update email address

            if formUpUser.profile_img.data or formUpUser.username.data or formUpUser.email.data:
                db.session.commit()  # update the user info
                flash('Sucessfully updated User info!', 'green')
            return redirect(url_for('users.account'))

    return render_template('dashboard/acc_settings.html', title='Account Settings', currentUsername=current_user.username, currentEmail=current_user.email, shortenForm=form, formUpUser=formUpUser, formUpPass=formUpPass)


# update user password
@users.route('/dashboard/account/update/password', methods=['POST'])
def update_userpass():
    formUpPass = UpdateUserPassword()

    if request.method == 'POST':
        if formUpPass.validate_on_submit():
            hashed_pass = bcrypt.generate_password_hash(formUpPass.new_pass.data).decode(
                "utf-8"
            )
            current_user.password = hashed_pass
            db.session.commit()
            flash('Sucessfully updated User password', 'green')
            return redirect(url_for('users.account'))
        else:
            return redirect(url_for('users.account'))   # redirect to the same route if there is a validation error in the password....
