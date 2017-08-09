from flask import Flask
from flask.ext.login import LoginManager


app = Flask(__name__)
app.config.from_object('config')
lm = LoginManager()
lm.init_app(app)

from app import views