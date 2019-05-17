"""
    Routes to handel reading list object in database
    By adding, editing, deleting and displaying 
    individual list with all books in the list in new page from database.
"""
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_required, current_user
from app import  db
from app.models import Lists, Book
from app.reading_list.forms import Add_Readinglist
from app.user.forms import LoginForm, RegisterForm

readinglists = Blueprint('readinglists', __name__, url_prefix='/reading_list')

# list of all reading lists
@readinglists.route('/readinglist', methods=['GET','POST'])
@login_required
def all_lists():
    form_list = Add_Readinglist()
    form_login = LoginForm()
    form_register = RegisterForm()
    reading_list = Lists.query.filter_by(UserId=current_user.id).all()
    return render_template('reading_list/reading_lists.html', form_list=form_list, title=current_user.name, reading_list=reading_list, form_login=form_login, form_register=form_register)
    
# add new reading list to database
@readinglists.route('/readinglist/add', methods=['GET','POST'])
@login_required
def add_readinglist():
    form_list = Add_Readinglist()
    form_login = LoginForm()
    form_register = RegisterForm()
    if form_list.validate_on_submit():
        readinglist = Lists(ListName=form_list.ListName.data, user=current_user )
        db.session.add(readinglist)
        db.session.commit()
        flash('New reading list has been added!', 'success')
    else:
            flash('Error: %s alredy have this list created.'%(current_user.name), 'danger ')
    reading_list = Lists.query.filter_by(UserId=current_user.id).all()
    return render_template('reading_list/reading_lists.html', form_list=form_list, title=current_user.name, reading_list=reading_list, form_login=form_login, form_register=form_register)  

# individual reading list with all books in the list
@readinglists.route('/readinglist/<int:list_id>')
@login_required
def one_list(list_id):
    form_login = LoginForm()
    form_register = RegisterForm()
    reading_list = Lists.query.get_or_404(list_id)
    return render_template('reading_list/reading_list.html', title=reading_list.ListName, reading_list=reading_list, form_login=form_login, form_register=form_register)
    
# edit reading list name
@readinglists.route('/readinglist/<int:list_id>/edit', methods=['GET','POST'])
@login_required
def edit_list(list_id):
    reading_list = Lists.query.get_or_404(list_id)
    form_list = Add_Readinglist()
    form_login = LoginForm()
    form_register = RegisterForm()
    if form_list.validate_on_submit():
        reading_list.ListName = form_list.ListName.data
        db.session.commit()
        flash('The list name has been updated!', 'success')
    elif request.method == 'GET': 
        form_list.ListName.data = reading_list.ListName
    else:
            flash('Error: User or other user alredy have this list created.','danger ')
    reading_list = Lists.query.filter_by(UserId=current_user.id).all()
    return render_template('reading_list/reading_lists.html', form_list=form_list, title=current_user.name, reading_list=reading_list, form_login=form_login, form_register=form_register) 
    
# delete reading list from database
@readinglists.route('/readinglist/<int:list_id>/delete', methods=['GET','POST'])
@login_required
def delete_list(list_id):
    reading_list = Lists.query.get_or_404(list_id)
    db.session.delete(reading_list)
    db.session.commit()
    flash('The list has been deleted!', 'success')
    return redirect(url_for('readinglists.all_lists'))
    
# delete book from rading list
@readinglists.route('/readinglist/<int:list_id>/delete_book/<int:book_id>', methods=['GET','POST'])
@login_required
def delete_book_in_list(list_id, book_id):
    reading_list = Lists.query.filter_by(id=list_id).first()
    book = Book.query.filter_by(isbn=book_id).first()
    print(book.title)
    reading_list.books_in_list.remove(book)
    db.session.commit()
    flash('The book has been deleted!', 'success')
    return redirect(url_for('readinglists.one_list', list_id=list_id))