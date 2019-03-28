"""
    Routes to handel book object in database
    By adding, editing, deleting and displaying 
    individual book in new page from database.
"""
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_required, current_user
from app import  db
from app.models import Book, Publisher, Category, Author, Lists
from app.book.forms import Add_Book, Add_book_to_readinglit

books = Blueprint('books', __name__, url_prefix='/book')

#add book    
@books.route('/book/add', methods=['GET','POST'])
@login_required
def add_book():
    all_publishers = Publisher.query.all()
    all_categories = Category.query.all()
    all_authors = Author.query.all()
    form = Add_Book()
    # passing all lists to form
    form.publisher.choices = [(p.PublisherId, p.Name) for p in all_publishers]
    form.category.choices = [(c.CategoryId, c.Name) for c in all_categories]
    form.author.choices = [(a.AuthorId, a.full_name) for a in all_authors]
    if form.validate_on_submit():
        book = Book(title=form.title.data, year=form.year.data, book_cover=form.book_cover.data, description=form.description.data, publisher_id=form.publisher.data, category_id=form.category.data)
        #author.writer.append(book)
        db.session.add(book)
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
        all_readinglits = Lists.query.filter_by(UserId=current_user.id).all()
        readinglists = [(l.id, l.ListName) for l in all_readinglits]
        form = Add_book_to_readinglit()
        # passing all lists to form
        form.lists.choices = readinglists
        print('*** lists *** %s' % readinglists)
        lists = form.lists.data
        print('*** lists in form *** %s' % lists)
        if form.validate_on_submit():
            book.books.append(lists)
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
        book.category_id = form.category.data
        book.category_id = form.category.data
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