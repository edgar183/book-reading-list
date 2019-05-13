from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from app import  db, bcrypt
from app.models import User, Lists, Book
from app.user.forms import RegisterForm, LoginForm, UpdateAccountForm

users = Blueprint('users', __name__, url_prefix='/user')

# register account page
@users.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form_register = RegisterForm()
    form_login = LoginForm()
    if form_register.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form_register.password.data)
        user = User(name=form_register.name.data, username=form_register.username.data, password=hash_password)
        db.session.add(user)
        db.session.commit()
        flash("%s your account has been created!"%(form_register.name.data), 'success')
        return redirect(url_for('main.index'))
    else:
        flash('Unsuccessful registraition. Please check information entered is corect.', 'danger')
    return render_template('user/register.html', form_register=form_register, form_login=form_login)  

# login to the system
@users.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('users.index'))
    form_login = LoginForm()
    form_register = RegisterForm()
    if form_login.validate_on_submit():
        # check user existst
        user = User.query.filter_by(username=form_login.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form_login.password.data):
            login_user(user, remember=form_login.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.index'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('user/login.html', title='Login', form_login=form_login, form_register=form_register)
    
#log out from system 
@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))
    
# account page where user can change account details    
@users.route('/account', methods=['GET','POST'])
@login_required
def account():
    form = UpdateAccountForm()
    form_login = LoginForm()
    form_register = RegisterForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.username = form.username.data
        db.session.commit()
        flash('Your account details has been updated!', 'success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.name.data = current_user.name
        form.username.data = current_user.username
    return render_template('user/account.html', title='Account', form=form, form_login=form_login, form_register=form_register )