from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from makemeshort import db, login_manager
from flask import current_app
from flask_login import UserMixin
from datetime import datetime
import nanoid  # for generating short urls


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    profile_img = db.Column(db.String(20), nullable=False,
                            server_default="default.jpg")
    password = db.Column(db.String(100), nullable=False)
    links = db.relationship('ShortenedLinks', backref='author', lazy=True)
    clicks = db.relationship('Clicks', backref='shortlink_author', lazy=True)

    def get_resetpass_token(self, expires=1800):
        __tk = Serializer(current_app.config['SECRET_KEY'], expires)
        return __tk.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_resetpass_token(token):
        __tk = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = __tk.loads(token)['user_id']
        except:
            return None

        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}')"


class ShortenedLinks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_made = db.Column(db.DateTime, nullable=False, default=datetime.now)
    long_url = db.Column(db.String(3000), nullable=False)
    shorten_url = db.Column(db.String(5), unique=True, nullable=False,
                            default=nanoid.generate(size=5))
    description = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    clicks = db.relationship('Clicks', backref='link', lazy=True)

    def __repr__(self):
        return f"Link('{self.id}', '{self.shorten_url}')"


class Clicks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_clicked = db.Column(db.DateTime, nullable=False, default=datetime.now)
    client_ip = db.Column(db.String(15), nullable=False)
    location = db.Column(db.String(50), nullable=True)
    referrer = db.Column(db.String(100), nullable=False)
    shortlink_id = db.Column(db.Integer, db.ForeignKey(
        'shortened_links.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Click('{self.id}', '{self.shortlink_id}')"


class QuickLinks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    longurl = db.Column(db.String(3000), nullable=False)
    datemade = db.Column(db.DateTime, nullable=False, default=datetime.now)
    shortlink = db.Column(db.String(7), unique=True,
                          nullable=False, default=nanoid.generate(size=7))

    def __repr__(self):
        return f"Quick_Link('{self.id}', '{self.shortlink}')"
