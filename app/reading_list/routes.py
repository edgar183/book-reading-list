"""
    Routes to handel reading list object in database
    By adding, editing, deleting and displaying 
    individual list with all books in the list in new page from database.
"""
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_required, current_user
from app import  db
from app.models import Lists
from app.reading_list.forms import Add_Readinglist

readinglists = Blueprint('readinglists', __name__, url_prefix='/reading_list')

# list of all reading lists
@readinglists.route('/readinglist', methods=['GET','POST'])
@login_required
def all_lists():
    reading_list = Lists.query.filter_by(UserId=current_user.id).all()
    return render_template('reading_list/reading_lists.html', title=current_user.name, reading_list=reading_list)
    
# add new readin list to database
@readinglists.route('/readinglist/add', methods=['GET','POST'])
@login_required
def add_readinglist():
    form = Add_Readinglist()
    if form.validate_on_submit():
        readinglist = Lists(ListName=form.ListName.data, user=current_user )
        db.session.add(readinglist)
        db.session.commit()
        flash('New reading list has been added!', 'success')
        return redirect(url_for('readinglists.all_lists'))
    return render_template('reading_list/add_readinglist.html', title='New Reading List', form=form, legend='Add New Reading List')   

# individual reading list route with all books in the list
@readinglists.route('/readinglist/<int:list_id>')
@login_required
def one_list(list_id):
    reading_list = Lists.query.get_or_404(list_id)
    return render_template('reading_list/reading_list.html', title=reading_list.ListName, reading_list=reading_list)
    
# edit reading list name
@readinglists.route('/readinglist/<int:list_id>/edit', methods=['GET','POST'])
@login_required
def edit_list(list_id):
    reading_list = Lists.query.get_or_404(list_id)
    form = Add_Readinglist()
    if form.validate_on_submit():
        reading_list.ListName = form.ListName.data
        db.session.commit()
        flash('The list name has been updated!', 'success')
        return redirect(url_for('readinglists.all_lists', list_id=reading_list.id))
    elif request.method == 'GET': 
        form.ListName.data = reading_list.ListName
    return render_template('reading_list/add_readinglist.html', title='Edit Reading Lits', form=form, legend='Edit List Name')
    
# delete reading list from database
@readinglists.route('/readinglist/<int:list_id>/delete', methods=['POST'])
@login_required
def delete_list(list_id):
    reading_list = Lists.query.get_or_404(list_id)
    db.session.delete(reading_list)
    db.session.commit()
    flash('The list has been deleted!', 'success')
    return redirect(url_for('readinglists.all_lists'))
    