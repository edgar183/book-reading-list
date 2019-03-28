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

authors = Blueprint('authors', __name__, url_prefix='/author')

# display list of authors
@authors.route('/authors')
def all_author():
    authors = Author.query.all()
    return render_template('author/authors.html', authors=authors, title='authors')
    
# individual author route
@authors.route('/authors/<int:author_id>')
@login_required
def single_author(author_id):
    author = Author.query.get_or_404(author_id)
    return render_template('author/author.html', title=author.full_name, author=author)
    
# add author to database   
@authors.route('/authors/add', methods=['GET','POST'])
@login_required
def add_author():
    form = Add_Author()
    if form.validate_on_submit():
        author = Author(full_name=form.full_name.data)
        db.session.add(author)
        db.session.commit()
        flash('New Author has been added!', 'success')
        return redirect(url_for('authors.all_author'))
    return render_template('author/add_author.html', title='New Author', form=form, legend='Add Author')
    
# edit author name
@authors.route('/authors/<int:author_id>/edit', methods=['GET','POST'])
@login_required
def edit_author(author_id):
    author = Author.query.get_or_404(author_id)
    form = Add_Author()
    if form.validate_on_submit():
        author.full_name = form.full_name.data
        db.session.commit()
        flash('The author name has been updated!', 'success')
        return redirect(url_for('authors.all_author', author_id=author.AuthorId))
    elif request.method == 'GET': 
        form.full_name.data = author.full_name
    return render_template('author/add_author.html', title='Edit Author ', form=form, legend='Edit Author')
    
# delete author from database
@authors.route('/authors/<int:author_id>/delete', methods=['POST'])
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
    page = request.args.get('page', 1, type=int)
    author_query = Author.query.filter_by(full_name=full_name).first_or_404()
    print('****author query -> %s' % author_query.AuthorId)
    
    books = Book.query.join(Book.authors).filter(Author.full_name == author_query.full_name).order_by(Book.isbn.desc()).paginate(page=page, per_page=6)

    print('***total books by author %s' % books.total)
    
   
    return render_template('author/author_books.html', books=books, author=author_query)