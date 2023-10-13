# app.py
# Codecademy Flask-Login

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, flash, render_template, redirect, request, url_for
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Keep it simple, stupid.'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))

@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    email = "bigmike"
    if request.form.get('password') == "5454160s":
        user = User(email="bigmike@foobar.com", username="Big_Mike",password="5454160s")
        login_user(user)
        return render_template('logged_in.html', current_user=user )
    else:
        flash("Incorrect username or password.")
        return redirect(url_for('index'))

@app.route('/home')
@login_required
def home():
	return render_template('logged_in.html')

@login_manager.unauthorized_handler
def unauthorized():
    return redirect('logout')

@app.route('/logout')
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for('index'))
    
@app.route('/about')
def about():
    return render_template('about.html')

def create_db():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    create_db()
    app.run(debug=True)

