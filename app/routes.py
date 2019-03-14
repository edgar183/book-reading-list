from flask import render_template, url_for, flash, redirect, request
from app import models
from app import app, db, bcrypt
from app.forms import RegisterForm, LoginForm, UpdateAccountForm, Add_Author
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
@app.route('/index')
def index():
    authors = models.Author.query.all()
    return render_template('index.html', authors=authors)

@app.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
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
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        # check user existst
        user = models.User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
    
@app.route('/account', methods=['GET','POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.username = form.username.data
        db.session.commit()
        flash('Your account details has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.name.data = current_user.name
        form.username.data = current_user.username
    return render_template('account.html', title='Account', form=form)
    
@app.route('/author/add', methods=['GET','POST'])
@login_required
def add_author():
    form = Add_Author()
    if form.validate_on_submit():
        # check user existst
        author = models.Author(full_name=form.full_name.data)
        db.session.add(author)
        db.session.commit()
        flash('New Author has been added!', 'success')
        return redirect(url_for('index'))
    return render_template('add_author.html', title='New Author', form=form)