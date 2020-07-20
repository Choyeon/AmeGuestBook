from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap


app = Flask('app')
app.config.from_pyfile('settings.py')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)
moment = Moment(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)

from app import views, errors, commands
"""
"""