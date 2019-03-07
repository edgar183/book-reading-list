from flask import render_template, url_for
from app import models
from app import app
from forms import RegisterForm, LoginForm

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    form = RegisterForm()
    return render_template('register.html', title='Register', form=form)    

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)
    

