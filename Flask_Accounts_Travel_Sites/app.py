# app.py

from os import environ
from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = "Let us get this done."

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get("DATABASE_URL") or 'sqlite:///my_database.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy()
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

import routes, models


if __name__ == '__main__':
    with app.app_context():
            db.create_all()
    app.run(debug=True)

