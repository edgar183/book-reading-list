from flask import render_template, url_for, flash, redirect
from app import models
from app import app
from app.forms import RegisterForm, LoginForm

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET','POST'])
def register():
    reg_form = RegisterForm()
    if reg_form.validate_on_submit():
        flash("Account created of user %s with username of %s!"%({reg_form.name.data}, {reg_form.username.data}), 'success')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=reg_form)    

@app.route('/login', methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        flash('%s You have been logged in!'%(login_form.username.data), 'success')
        return redirect(url_for('index'))
    else:
        flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=login_form)
    

