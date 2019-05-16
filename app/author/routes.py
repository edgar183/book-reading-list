"""
    Routes to handel author object in database
    By adding, editing, deleting and displaying 
    list of all publishers from database.
"""
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_required
from app import  db
from app.models import Author, Book
from app.author.forms import Add_Author
from app.book.forms import Add_Book
from app.category.forms import Add_Category
from app.publisher.forms import Add_Publisher
from app.user.forms import LoginForm, RegisterForm

authors = Blueprint('authors', __name__, url_prefix='/author')

# display list of authors
@authors.route('/authors')
@login_required
def all_author():
    form_author = Add_Author()
    form_login = LoginForm()
    form_register = RegisterForm()
    authors = Author.query.all()
    return render_template('author/authors.html', authors=authors, title='Authors', form_author=form_author, form_login=form_login, form_register=form_register)

# add author to database   
@authors.route('/book/add', methods=['GET','POST'])
@login_required
def add_author():
    form = Add_Book()
    form_login=LoginForm()
    form_register=RegisterForm()
    form_cat = Add_Category()
    form_publisher = Add_Publisher()
    form_author = Add_Author()
    if form_author.validate_on_submit():
        author = Author(full_name=form_author.full_name.data)
        db.session.add(author)
        db.session.commit()
        flash('New Author has been added!', 'success')
    else:
        flash('Error: The author with this name alredy exists!', 'danger ')
    return render_template('book/add_book.html', title='New Book', form=form, legend='Add Book', form_login=form_login, form_register=form_register, form_cat=form_cat, form_publisher=form_publisher, form_author=form_author)
    
# edit author name
@authors.route('/authors/<int:author_id>/edit', methods=['GET','POST'])
@login_required
def edit_author(author_id):
    author = Author.query.get_or_404(author_id)
    form_author = Add_Author()
    form_login = LoginForm()
    form_register = RegisterForm()
    if form_author.validate_on_submit():
        author.full_name = form_author.full_name.data
        db.session.commit()
        flash('The author name has been updated!', 'success')
        return redirect(url_for('authors.all_author', author_id=author.AuthorId))
    elif request.method == 'GET': 
        form_author.full_name.data = author.full_name
    else:
            flash('Error: The author with this name alredy exists!', 'danger ')
    authors = Author.query.all()
    return render_template('author/authors.html', authors=authors, title='Authors', form_author=form_author, form_login=form_login, form_register=form_register)
    
# delete author from database
@authors.route('/authors/<int:author_id>/delete', methods=['GET','POST'])
@login_required
def delete_author(author_id):
    author = Author.query.get_or_404(author_id)
    db.session.delete(author)
    db.session.commit()
    flash('The author has been deleted!', 'success')
    return redirect(url_for('authors.all_author'))

# display all books from the author    
@authors.route('/author/<string:full_name>')
def author_books(full_name):
    form_login = LoginForm()
    form_register = RegisterForm()
    page = request.args.get('page', 1, type=int)
    author_query = Author.query.filter_by(full_name=full_name).first_or_404()
    books = Book.query.join(Book.author).filter(Author.full_name == author_query.full_name).order_by(Book.isbn.desc()).paginate(page=page, per_page=6)
    return render_template('author/author_books.html', books=books, author=author_query, form_login=form_login, form_register=form_register)