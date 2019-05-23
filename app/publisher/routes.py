"""
    Routes to handel publishre object in database
    By adding, editing, deleting and displaying 
    list of all publishers from database.
"""
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_required
from app import  db
from app.models import Publisher, Book
from app.author.forms import Add_Author
from app.book.forms import Add_Book
from app.category.forms import Add_Category
from app.publisher.forms import Add_Publisher
from app.user.forms import LoginForm, RegisterForm

publishers = Blueprint('publishers', __name__, url_prefix='/publisher')

# display list of publishers
@publishers.route('/publisher')
@login_required
def all_publishers():
    form_publisher = Add_Publisher()
    form_login = LoginForm()
    form_register = RegisterForm()
    publishers = Publisher.query.all()
    return render_template('publisher/publishers.html', form_publisher=form_publisher, publishers=publishers, title='Publishers', form_login=form_login, form_register=form_register)

#add publisher    
@publishers.route('/publishers/add', methods=['POST'])
@login_required
def add_publisher():
    form_publisher = Add_Publisher()
    if request.method == 'POST':
        publisherName = request.form['publisherName']
        publisher = Publisher(publisherName=publisherName)
        db.session.add(publisher)
        db.session.commit()
        flash('New publisher name has been added!', 'success')
    elif form_publisher.validate_on_submit():
        flash('Error: The publisher alredy exists!', 'danger ')
    form = Add_Book()
    return render_template('publisher/publisher_options.html', form=form )
    
# edit publishers name
@publishers.route('/publisher/<int:publisher_id>/edit', methods=['GET','POST'])
@login_required
def edit_publisher(publisher_id):
    publisher = Publisher.query.get_or_404(publisher_id)
    form_publisher = Add_Publisher()
    form_login = LoginForm()
    form_register = RegisterForm()
    if form_publisher.validate_on_submit():
        publisher.publisherName = form_publisher.publisherName.data
        db.session.commit()
        flash('The publisher publisherName has been updated!', 'success')
        return redirect(url_for('publishers.all_publishers', publisher_id=publisher.PublisherId))
    elif request.method == 'GET': 
        form_publisher.publisherName.data = publisher.publisherName
    else:
            flash('Error: The publisher alredy exists!', 'danger ')
    publishers = Publisher.query.all()
    return render_template('publisher/publishers.html', form_publisher=form_publisher, publishers=publishers, title='Publishers', form_login=form_login, form_register=form_register)
    
# delete publishers from database
@publishers.route('/publisher/<int:publisher_id>/delete',  methods=['GET','POST'])
@login_required
def delete_publisher(publisher_id):
    publisher = Publisher.query.get_or_404(publisher_id)
    db.session.delete(publisher)
    db.session.commit()
    flash('The publisher has been deleted!', 'success')
    return redirect(url_for('publishers.all_publishers'))
    
# display all books from the publisher    
@publishers.route('/publisher/<string:publisherName>')
def publisher_books(publisherName):
    form_login = LoginForm()
    form_register = RegisterForm()
    page = request.args.get('page', 1, type=int)
    publisher_query = Publisher.query.filter_by(publisherName=publisherName).first_or_404()
    books = Book.query.filter_by(publisher=publisher_query).order_by(Book.isbn.desc()).paginate(page=page, per_page=6)
    return render_template('publisher/publisher_books.html',books=books, publisher=publisher_query, form_login=form_login, form_register=form_register)
