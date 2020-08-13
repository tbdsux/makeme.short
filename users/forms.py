from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import (
    DataRequired,
    Length,
    Email,
    EqualTo,
    ValidationError,
    Regexp,
)
from flask_login import current_user
from makemeshort.models import User


class RegisterForm(FlaskForm):
    username = StringField('Username:', validators=[
                           DataRequired(message="Username is required!"), Length(min=3, max=15, message="Username is too short / long!"), Regexp(r"^[\w.@+-]+$", message="Username cannot contain blank spaces!")])
    email = StringField('Email Address:', validators=[DataRequired(
        message="Email address is required!"), Email(message="Invalid Email address!")])
    password = PasswordField('Password:', validators=[
                             DataRequired(message="Password is required!")])
    confirm_password = PasswordField(
        'Confirm Password:', validators=[DataRequired(message="Confirm your password!"), EqualTo("password", message="Passwords are not equal!")]
    )
    agree = BooleanField('I Agree to the')

    register = SubmitField('Create Account')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is already taken.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                'An account is currently registered with that email address.')


class LoginForm(FlaskForm):
    username = StringField('Username:', validators=[
                           DataRequired(message="Username is required!"), Regexp(r"^[\w.@+-]+$", message="Username cannot contain blank spaces!")])
    password = PasswordField('Password:', validators=[
                             DataRequired(message="Password is required!")])
    remember = BooleanField('Remember Me')
    login = SubmitField('Log In')


class UpdateUserInfo(FlaskForm):
    profile_img = FileField('Profile Image', validators=[
                            FileAllowed(['jpg', 'png'])])
    username = StringField('Username:', validators=[
                           DataRequired(message="Username is required!"), Length(min=3, max=15, message="Username is too short / long!"), Regexp(r"^[\w.@+-]+$", message="Username cannot contain blank spaces!")])
    email = StringField('Email Address:', validators=[DataRequired(
        message="Email address is required!"), Email(message="Invalid Email address!")])
    save = SubmitField('Save Changes')

    def validate_username(self, username):
        if not current_user.username == username.data:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Username is already taken.')

    def validate_email(self, email):
        if not current_user.email == email.data:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError(
                    'An account is currently registered with that email address.')


class UpdateUserPassword(FlaskForm):
    new_pass = PasswordField('Password:', validators=[
                             DataRequired(message="Password is required!")])
    confirm_new_pass = PasswordField(
        'Confirm Password:', validators=[DataRequired(message="Confirm your password!"), EqualTo("password", message="Passwords are not equal!")]
    )
    update = SubmitField('Update Password')


class ForgotPassReqForm(FlaskForm):
    email = StringField('Email Address:', validators=[DataRequired(
        message="Email address is required!"), Email(message="Invalid Email address!")])

    request = SubmitField('Send Request')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError(
                'There is no user registered with that email address!')


class EnterNewPassForm(FlaskForm):
    password = PasswordField('New Password', validators=[DataRequired(
        message="Password is required!"), Length(min=8, message="Password is too short!")])
    confirm_password = PasswordField(
        'Confirm New Password', validators=[DataRequired(message="Confirm your new password!"), EqualTo("password", message="Passwords are not equal!")]
    )
    update = SubmitField('Update Password')
