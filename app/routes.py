from flask import render_template, url_for, flash, redirect, request
from app import models
from app.models import *
from app import app, db, bcrypt
from app.forms import RegisterForm, LoginForm, UpdateAccountForm, Add_Author, Add_Category, Add_Publisher, Add_Readinglist, Add_Book
from flask_login import login_user, current_user, logout_user, login_required

# home page
@app.route('/')
@app.route('/index')
def index():
    books = Book.query.all()
    return render_template('index.html',books=books)

# register account page
@app.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name=form.name.data, username=form.username.data, password=hash_password)
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
        user = User.query.filter_by(username=form.username.data).first()
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
    readinglists = Lists.query.all()
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
"""
    Routes to handel author object in database
    By adding, editing, deleting and displaying 
    list of all publishers from database.
"""
# display list of authors
@app.route('/authors')
def authors():
    authors = Author.query.all()
    return render_template('authors.html', authors=authors, title='authors')
    
# individual author route
@app.route('/authors/<int:author_id>')
@login_required
def author(author_id):
    author = Author.query.get_or_404(author_id)
    return render_template('author.html', title=author.full_name, author=author)
    
# add author to database   
@app.route('/authors/add', methods=['GET','POST'])
@login_required
def add_author():
    form = Add_Author()
    if form.validate_on_submit():
        author = Author(full_name=form.full_name.data)
        db.session.add(author)
        db.session.commit()
        flash('New Author has been added!', 'success')
        return redirect(url_for('authors'))
    return render_template('add_author.html', title='New Author', form=form, legend='Add Author')
    
# edit author name
@app.route('/authors/<int:author_id>/edit', methods=['GET','POST'])
@login_required
def edit_author(author_id):
    author = Author.query.get_or_404(author_id)
    form = Add_Author()
    if form.validate_on_submit():
        author.full_name = form.full_name.data
        db.session.commit()
        flash('The author name has been updated!', 'success')
        return redirect(url_for('authors', author_id=author.AuthorId))
    elif request.method == 'GET': 
        form.full_name.data = author.full_name
    return render_template('add_author.html', title='Edit Author ', form=form, legend='Edit Author')

# delete author from database
@app.route('/authors/<int:author_id>/delete', methods=['POST'])
@login_required
def delete_author(author_id):
    author = Author.query.get_or_404(author_id)
    db.session.delete(author)
    db.session.commit()
    flash('The author has been deleted!', 'success')
    return redirect(url_for('authors'))
"""
    Routes to handel category object in database
    By adding, editing, deleting and displaying 
    list of all publishers from database.
"""
# display list of categories
@app.route('/categories')
def categories():
    categories = Category.query.all()
    return render_template('categories.html', categories=categories, title='categories')
    
# individual category route
@app.route('/categories/<int:category_id>')
@login_required
def category(category_id):
    category = Category.query.get_or_404(category_id)
    return render_template('category.html', title=category.Name, category=category)

# add category     
@app.route('/categories/add', methods=['GET','POST'])
@login_required
def add_category():
    form = Add_Category()
    if form.validate_on_submit():
        category = Category(Name=form.Name.data)
        db.session.add(category)
        db.session.commit()
        flash('New Category has been added!', 'success')
        return redirect(url_for('categories'))
    return render_template('add_category.html', title='New Category', form=form, legend='Add New Category')

# edit category name
@app.route('/categories/<int:category_id>/edit', methods=['GET','POST'])
@login_required
def edit_category(category_id):
    category = Category.query.get_or_404(category_id)
    form = Add_Category()
    if form.validate_on_submit():
        category.Name = form.Name.data
        db.session.commit()
        flash('The category name has been updated!', 'success')
        return redirect(url_for('categories', category_id=category.CategoryId))
    elif request.method == 'GET': 
        form.Name.data = category.Name
    return render_template('add_category.html', title='Edit Category ', form=form, legend='Edit Category Name')

# delete category from database
@app.route('/categories/<int:category_id>/delete', methods=['POST'])
@login_required
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    flash('The category has been deleted!', 'success')
    return redirect(url_for('categories'))
    
"""
    Routes to handel publishre object in database
    By adding, editing, deleting and displaying 
    list of all publishers from database.
"""
# display list of publishers
@app.route('/publishers')
@login_required
def publishers():
    publishers = Publisher.query.all()
    return render_template('publishers.html', publishers=publishers, title='Publishers')
    
# individual publisher route
@app.route('/publishers/<int:publisher_id>')
@login_required
def publisher(publisher_id):
    publisher = Publisher.query.get_or_404(publisher_id)
    return render_template('publisher.html', title=publisher.Name, publisher=publisher)
    
#add publisher    
@app.route('/publishers/add', methods=['GET','POST'])
@login_required
def add_publisher():
    form = Add_Publisher()
    if form.validate_on_submit():
        publisher = Publisher(Name=form.Name.data)
        db.session.add(publisher)
        db.session.commit()
        flash('New Publisher has been added!', 'success')
        return redirect(url_for('publishers'))
    return render_template('add_publisher.html', title='New Publisher', form=form, legend='Add Publisher Name')
    
# edit publishers name
@app.route('/publishers/<int:publisher_id>/edit', methods=['GET','POST'])
@login_required
def edit_publisher(publisher_id):
    publisher = Publisher.query.get_or_404(publisher_id)
    form = Add_Publisher()
    if form.validate_on_submit():
        publisher.Name = form.Name.data
        db.session.commit()
        flash('The publisher name has been updated!', 'success')
        return redirect(url_for('publishers', publisher_id=publisher.PublisherId))
    elif request.method == 'GET': 
        form.Name.data = publisher.Name
    return render_template('add_publisher.html', title='Edit Publisher ', form=form, legend='Edit Publisher Name')
    
# delete publishers from database
@app.route('/publishers/<int:publisher_id>/delete', methods=['POST'])
@login_required
def delete_publisher(publisher_id):
    publisher = Publisher.query.get_or_404(publisher_id)
    db.session.delete(publisher)
    db.session.commit()
    flash('The publisher has been deleted!', 'success')
    return redirect(url_for('publishers'))

"""
    Routes to handel reading list object in database
    By adding, editing, deleting and displaying 
    individual list with all books in the list in new page from database.
"""
# add new readin list to database
@app.route('/readinglist/add', methods=['GET','POST'])
@login_required
def add_readinglist():
    form = Add_Readinglist()
    if form.validate_on_submit():
        readinglist = Lists(ListName=form.ListName.data, user=current_user )
        db.session.add(readinglist)
        db.session.commit()
        flash('New reading list has been added!', 'success')
        return redirect(url_for('account'))
    return render_template('add_readinglist.html', title='New Reading List', form=form, legend='Add New Reading List')   

# individual reading list route with all books in the list
@app.route('/readinglist/<int:list_id>')
@login_required
def reading_list(list_id):
    reading_list = Lists.query.get_or_404(list_id)
    return render_template('reading_list.html', title=reading_list.ListName, reading_list=reading_list)
    
# edit reading list name
@app.route('/readinglist/<int:list_id>/edit', methods=['GET','POST'])
@login_required
def edit_list(list_id):
    reading_list = Lists.query.get_or_404(list_id)
    form = Add_Readinglist()
    if form.validate_on_submit():
        reading_list.ListName = form.ListName.data
        db.session.commit()
        flash('The list name has been updated!', 'success')
        return redirect(url_for('reading_list', list_id=reading_list.id))
    elif request.method == 'GET': 
        form.ListName.data = reading_list.ListName
    return render_template('add_readinglist.html', title='Edit Reading Lits', form=form, legend='Edit List Name')
    
# delete reading list from database
@app.route('/readinglist/<int:list_id>/delete', methods=['POST'])
@login_required
def delete_list(list_id):
    reading_list = Lists.query.get_or_404(list_id)
    db.session.delete(reading_list)
    db.session.commit()
    flash('The list has been deleted!', 'success')
    return redirect(url_for('account'))
    
"""
    Routes to handel book object in database
    By adding, editing, deleting and displaying 
    individual book in new page from database.
"""
#add book    
@app.route('/book/add', methods=['GET','POST'])
@login_required
def add_book():
    form = Add_Book()
    form.publisher.choices = [(publisher.PublisherId, publisher.Name) for publisher in Publisher.query.all()]
    form.category.choices = [(category.CategoryId, category.Name) for category in Category.query.all()]
    form.author.choices = [(author.AuthorId, author.full_name) for author in Author.query.all()]
    publisher = Publisher.query.filter_by(PublisherId=form.publisher.data)
    category = Category.query.filter_by(CategoryId=form.category.data)
    author = Author.query.filter_by(AuthorId=form.author.data)
    if form.validate_on_submit():
        book = Book(title=form.title.data, year=form.year.data, book_cover=form.book_cover.data, description=form.description.data, publisher_id=publisher, category_id=category, author_id=author)
        db.session.add(book)
        db.session.commit()
        flash('New Book has been added!', 'success')
        return redirect(url_for('index'))
    return render_template('add_book.html', title='New Book', form=form, legend='Add Book')
    
# individual book page
@app.route('/book/<int:book_isbn>')
def book(book_isbn):
    book = Book.query.get_or_404(book_isbn)
    readinglists = Lists.query.all()
    return render_template('book.html', title=book.title, book=book, readinglists=readinglists)
    
# edit book information
@app.route('/book/<int:book_isbn>/edit', methods=['GET','POST'])
@login_required
def edit_book(book_isbn):
    book = Book.query.get_or_404(book_isbn)
    form = Add_Book()
    if form.validate_on_submit():
        book.title = form.title.data
        book.year = form.year.data
        book.book_cover = form.book_cover.data
        book.description = form.description.data
        book.category_id = form.category.data
        book.category_id = form.category.data
        db.session.commit()
        flash('The book detailes has been edited!', 'success')
        return redirect(url_for('book', book_isbn=book.isbn))
    elif request.method == 'GET':    
        form.title.data = book.title
        form.year.data = book.year
        form.book_cover.data = book.book_cover
        form.description.data = book.description
        form.publisher.data = book.publisher
        form.category.data = book.category
    return render_template('add_book.html', title='Edit Book', form=form, legend='Edit Book')
    
# delete book from database
@app.route('/book/<int:book_isbn>/delete', methods=['POST'])
@login_required
def delete_book(book_isbn):
    book = Book.query.get_or_404(book_isbn)
    db.session.delete(book)
    db.session.commit()
    flash('The book has been deleted!', 'success')
    return redirect(url_for('index'))