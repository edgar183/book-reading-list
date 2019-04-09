"""
    Routes to handel book object in database
    By adding, editing, deleting and displaying 
    individual book in new page from database.
"""
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_required, current_user
from app import  db
from app.models import *
from app.book.forms import Add_Book, Add_book_to_readinglit

books = Blueprint('books', __name__, url_prefix='/book')

#add book    
@books.route('/book/add', methods=['GET','POST'])
@login_required
def add_book():
    form = Add_Book()
    author = form.author.data
    publisher = form.publisher.data
    category = form.category.data
    if form.validate_on_submit():
        book = Book(title=form.title.data, year=form.year.data, book_cover=form.book_cover.data, description=form.description.data, publisher_id=publisher.PublisherId, category_id=category.CategoryId)
        db.session.add(book)
        author.writer.append(book)
        db.session.commit()
        flash('New Book has been added!', 'success')
        return redirect(url_for('main.index'))
    return render_template('book/add_book.html', title='New Book', form=form, legend='Add Book')
    
# individual book page
# add book to reading list
@books.route('/book/<int:book_isbn>', methods=['GET','POST'])
def book(book_isbn):
    book = Book.query.get_or_404(book_isbn)
    if current_user.is_authenticated:
        form = Add_book_to_readinglit()
        selected_list = form.lists.data
        print('*** selected list object *** %s *** and book %s' % (selected_list, book))
        if form.validate_on_submit():
            book.books.append(selected_list)
            db.session.commit()
            flash('New Book has been added to list!', 'success')
            return redirect(url_for('main.index'))
        return render_template('book/book.html', title=book.title, book=book, form=form)
    return render_template('book/book.html', title=book.title, book=book)
    
# edit book information
@books.route('/book/<int:book_isbn>/edit', methods=['GET','POST'])
@login_required
def edit_book(book_isbn):
    book = Book.query.get_or_404(book_isbn)
    form = Add_Book()
    if form.validate_on_submit():
        book.title = form.title.data
        book.year = form.year.data
        book.book_cover = form.book_cover.data
        book.description = form.description.data
        publisher = form.publisher.data
        book.publisher_id = publisher.PublisherId
        category = form.category.data
        book.category_id = category.CategoryId
        #author = form.author.data
        #book.authors = author.AuthorId
        db.session.commit()
        flash('The book detailes has been edited!', 'success')
        return redirect(url_for('books.book', book_isbn=book.isbn))
    elif request.method == 'GET':    
        form.title.data = book.title
        form.year.data = book.year
        form.book_cover.data = book.book_cover
        form.description.data = book.description
        form.publisher.data = book.publisher
        form.category.data = book.category
        for author in book.authors:
            book_author=author.full_name
        form.author.data = book_author
    return render_template('book/add_book.html', title='Edit Book', form=form, legend='Edit Book')
    
# delete book from database
@books.route('/book/<int:book_isbn>/delete', methods=['POST'])
@login_required
def delete_book(book_isbn):
    book = Book.query.get_or_404(book_isbn)
    db.session.delete(book)
    db.session.commit()
    flash('The book has been deleted!', 'success')
    return redirect(url_for('main.index'))