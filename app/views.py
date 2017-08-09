from flask import render_template, flash, url_for, redirect, g
from flask_login import current_user
from app import app, lm
from .forms import LoginForm

@app.before_request
def before_request():
    g.user = 'Александр'

@app.route('/')
@app.route('/index')
def index():
    if g.user is not None:
        return render_template("index.html", user=g.user,
            title='GM-TOKEN')
    return redirect(url_for('login'))

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('login.html', 
        title = 'Sign In',
        form = form)