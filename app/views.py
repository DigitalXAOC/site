from flask import render_template, flash, url_for, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", user='Александр',
    	title='GM-TOKEN')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('HELLO')
        return redirect(url_for('index'))
    flash(form.validate_on_submit())
    return render_template('login.html', 
        title = 'Sign In',
        form = form)