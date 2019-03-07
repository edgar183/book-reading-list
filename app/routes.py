from flask import render_template, url_for, flash, redirect
from app import models
from app import app
from app.forms import RegisterForm, LoginForm

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash("Account created of user %s with username of %s!"%({form.name.data}, {form.username.data}), 'success')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)    

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('%s You have been logged in!'%(form.username.data), 'success')
        return redirect(url_for('index'))
    else:
        flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
    

