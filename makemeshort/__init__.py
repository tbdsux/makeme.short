from flask import Flask, abort
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, current_user
from flask_mail import Mail
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from functools import wraps
from makemeshort.config import Development, Production

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'blue'
login_manager.session_protection = 'strong'
mail = Mail()
csrf = CSRFProtect()


def create_app(config_class=Production):
    app = Flask(__name__)
    app.config.from_object(Production)  # use 'Production' in production mode
    app.url_map.strict_slashes = False  # allow trailing slashes in routes

    db.init_app(app)
    migrate = Migrate(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    csrf.init_app(app)

    from makemeshort.index.routes import index
    from makemeshort.users.routes import users
    from makemeshort.links.routes import links

    app.register_blueprint(index)
    app.register_blueprint(users)
    app.register_blueprint(links)

    return app
