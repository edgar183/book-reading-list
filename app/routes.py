from flask import render_template, url_for, flash, redirect
from app import models
from app import app, db, bcrypt
from app.forms import RegisterForm, LoginForm

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = models.User(name=form.name.data, username=form.username.data, password=hash_password)
        db.session.add(user)
        db.session.commit()
        flash("%s your account has been created!"%(form.name.data), 'success')
        return redirect(url_for('login'))
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
    

