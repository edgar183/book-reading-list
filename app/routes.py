from flask import render_template, url_for
from app import models
from app import app
from app.forms import RegisterForm, LoginForm

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET','POST'])
def register():
    reg_form = RegisterForm()
    return render_template('register.html', title='Register', form=reg_form)    

@app.route('/login', methods=['GET','POST'])
def login():
    login_form = LoginForm()
    return render_template('login.html', title='Login', form=login_form)
    

