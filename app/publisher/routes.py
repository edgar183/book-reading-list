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
@publishers.route('/publishers/add', methods=['GET','POST'])
@login_required
def add_publisher():
    form = Add_Book()
    form_login=LoginForm()
    form_register=RegisterForm()
    form_cat = Add_Category()
    form_publisher = Add_Publisher()
    form_author = Add_Author()
    if form_publisher.validate_on_submit():
        publisher = Publisher(Name=form_publisher.Name.data)
        db.session.add(publisher)
        db.session.commit()
        flash('New Publisher has been added!', 'success')
    else:
            flash('Error: The publisher alredy exists!', 'danger ')
    return render_template('book/add_book.html', title='New Book', form=form, legend='Add Book', form_login=form_login, form_register=form_register, form_cat=form_cat, form_publisher=form_publisher, form_author=form_author)
    
# edit publishers name
@publishers.route('/publisher/<int:publisher_id>/edit', methods=['GET','POST'])
@login_required
def edit_publisher(publisher_id):
    publisher = Publisher.query.get_or_404(publisher_id)
    form_publisher = Add_Publisher()
    form_login = LoginForm()
    form_register = RegisterForm()
    if form_publisher.validate_on_submit():
        publisher.Name = form_publisher.Name.data
        db.session.commit()
        flash('The publisher name has been updated!', 'success')
        return redirect(url_for('publishers.all_publishers', publisher_id=publisher.PublisherId))
    elif request.method == 'GET': 
        form_publisher.Name.data = publisher.Name
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
@publishers.route('/publisher/<string:Name>')
def publisher_books(Name):
    form_login = LoginForm()
    form_register = RegisterForm()
    page = request.args.get('page', 1, type=int)
    publisher_query = Publisher.query.filter_by(Name=Name).first_or_404()
    books = Book.query.filter_by(publisher=publisher_query).order_by(Book.isbn.desc()).paginate(page=page, per_page=6)
    return render_template('publisher/publisher_books.html',books=books, publisher=publisher_query, form_login=form_login, form_register=form_register)
