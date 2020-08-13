from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL, Regexp


class ShortenLinkForm(FlaskForm):
    link = StringField('Your URL', validators=[DataRequired(message="Enter a URL to make a shortlink."), Regexp(
        r"^(?:(?:(?:https?|ftp):)?\/\/)(?:\S+(?::\S*)?@)?(?:(?!(?:10|127)(?:\.\d{1,3}){3})(?!(?:169\.254|192\.168)(?:\.\d{1,3}){2})(?!172\.(?:1[6-9]|2\d|3[0-1])(?:\.\d{1,3}){2})(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))|(?:(?:[a-z0-9\u00a1-\uffff][a-z0-9\u00a1-\uffff_-]{0,62})?[a-z0-9\u00a1-\uffff]\.)+(?:[a-z\u00a1-\uffff]{2,}\.?))(?::\d{2,5})?(?:[/?#]\S*)?$", message="Invalid URL Address!")])
    description = StringField('Description')
    shorten = SubmitField('Shorten Link')


class DirectShortenLinkForm(FlaskForm):
    link = StringField('Your Long URL', validators=[DataRequired(message="Enter a URL to make a shortlink."), URL(message="Invalid URL Address!")])
    direct_shorten = SubmitField('Quick Shorten')


class DeleteLinkForm(FlaskForm):
    delete = SubmitField('Delete')


class UpdateLinkDescriptionForm(FlaskForm):
    description = StringField('New Shortlink Description')
    update = SubmitField('Update')
