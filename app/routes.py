from flask import render_template, url_for, flash, redirect, request
from app import models
from app import app, db, bcrypt
from app.forms import RegisterForm, LoginForm, UpdateAccountForm, Add_Author, Add_Category, Add_Publisher, Add_Readinglist, Add_Book
from flask_login import login_user, current_user, logout_user, login_required

# home page
@app.route('/')
@app.route('/index')
def index():
    authors = models.Author.query.all()
    publishers = models.Publisher.query.all()
    categories = models.Category.query.all()
    users = models.User.query.all()
    readinglists = models.Lists.query.all()
    books = models.Book.query.all()
    return render_template('index.html', authors=authors, publishers=publishers, categories=categories, users=users, readinglists=readinglists, books=books)

# register account page
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

# login to the system
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

#log out from system 
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

# account page where user can change account details    
@app.route('/account', methods=['GET','POST'])
@login_required
def account():
    form = UpdateAccountForm()
    readinglists = models.Lists.query.all()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.username = form.username.data
        db.session.commit()
        flash('Your account details has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.name.data = current_user.name
        form.username.data = current_user.username
    return render_template('account.html', title='Account', form=form, readinglists=readinglists)

# add author to database   
@app.route('/author/add', methods=['GET','POST'])
@login_required
def add_author():
    form = Add_Author()
    if form.validate_on_submit():
        author = models.Author(full_name=form.full_name.data)
        db.session.add(author)
        db.session.commit()
        flash('New Author has been added!', 'success')
        return redirect(url_for('index'))
    return render_template('add_author.html', title='New Author', form=form)

# add new category     
@app.route('/category/add', methods=['GET','POST'])
@login_required
def add_category():
    form = Add_Category()
    if form.validate_on_submit():
        category = models.Category(Name=form.Name.data)
        db.session.add(category)
        db.session.commit()
        flash('New Category has been added!', 'success')
        return redirect(url_for('index'))
    return render_template('add_category.html', title='New Category', form=form)

#add publisher    
@app.route('/publisher/add', methods=['GET','POST'])
@login_required
def add_publisher():
    form = Add_Publisher()
    if form.validate_on_submit():
        publisher = models.Publisher(Name=form.Name.data)
        db.session.add(publisher)
        db.session.commit()
        flash('New Publisher has been added!', 'success')
        return redirect(url_for('index'))
    return render_template('add_publisher.html', title='New Publisher', form=form)

# add new readin list to database
@app.route('/readinglist/add', methods=['GET','POST'])
@login_required
def add_readinglist():
    form = Add_Readinglist()
    if form.validate_on_submit():
        # check user existst
        readinglist = models.Lists(ListName=form.ListName.data, user=current_user )
        db.session.add(readinglist)
        db.session.commit()
        flash('New reading list has been added!', 'success')
        return redirect(url_for('account'))
    return render_template('add_readinglist.html', title='New Reading List', form=form)   
#author=current_user.name

#add book    
@app.route('/book/add', methods=['GET','POST'])
@login_required
def add_book():
    form = Add_Book()
    form.publisher.choices = [(publisher.PublisherId, publisher.Name) for publisher in models.Publisher.query.all()]
    form.category.choices = [(category.CategoryId, category.Name) for category in models.Category.query.all()]
    #publisher = models.Publisher.query.filter_by(PublisherId=form.publisher.data)
    #category = models.Category.query.filter_by(CategoryId=form.category.data)
    if form.validate_on_submit():
        book = models.Book(title=form.title.data, year=form.year.data, book_cover=form.book_cover.data, description=form.description.data, publisher_id=models.Publisher.query.filter_by(PublisherId=form.publisher.data), category_id=models.Category.query.filter_by(CategoryId=form.category.data))
        db.session.add(book)
        db.session.commit()
        flash('New Book has been added!', 'success')
        return redirect(url_for('index'))
    return render_template('add_book.html', title='New Book', form=form)
    
# individual book page
@app.route('/book/<int:book_isbn>')
def book(book_isbn):
    book = models.Book.query.get_or_404(book_isbn)
    return render_template('book.html', title=book.title, book=book)