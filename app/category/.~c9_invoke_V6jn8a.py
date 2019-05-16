"""
    Routes to handel category object in database
    By adding, editing, deleting and displaying 
    list of all publishers from database.
"""
from flask import render_template, url_for, flash, redirect, request, Blueprint, jsonify
from flask_login import login_required
from app import  db
from app.models import Category, Book
from app.category.forms import Add_Category
from app.book.forms import Add_Book
from app.publisher.forms import Add_Publisher
from app.author.forms import Add_Author
from app.user.forms import LoginForm, RegisterForm

categories = Blueprint('categories', __name__, url_prefix='/category')

# display list of categories
@categories.route('/categories')
@login_required
def all_categories():
    form_cat = Add_Category()
    form_login = LoginForm() 
    form_register = RegisterForm()
    categories = Category.query.all()
    return render_template('category/categories.html', categories=categories, title='Categories', form_cat=form_cat, form_login=form_login, form_register=form_register)

# add category     
@categories.route('/categories/add', methods=['POST'])
@login_required
def add_category():
    form_login=LoginForm()
    form_register=RegisterForm() 
    form_cat = Add_Category()
    if form_cat.validate_on_submit():
        category = Category(Name=form_cat.Name.data)
        db.session.add(category)
        db.session.commit()
        flash('New Category has been added!', 'success')
    else:
        flash('Error: The category alredy exists!', 'danger ')
        return jsonify(data=form_cat.errors)
    #categories = Category.query.all()
    #return render_template('category/categories.html', categories=categories, title='Categories', form_cat=form_cat, form_login=form_login, form_register=form_register)
    
# edit category name
@categories.route('/categories/<int:category_id>/edit', methods=['GET','POST'])
@login_required
def edit_category(category_id):
    category = Category.query.get_or_404(category_id)
    form_cat = Add_Category()
    form_login = LoginForm()
    form_register = RegisterForm()
    if form_cat.validate_on_submit():
        category.Name = form_cat.Name.data
        db.session.commit()
        flash('The category name has been updated!', 'success')
    elif request.method == 'GET': 
        form_cat.Name.data = category.Name
    else:
            flash('Error: The category alredy exists!', 'danger ')
    categories = Category.query.all()
    return render_template('category/categories.html', categories=categories, title='Categories', form_cat=form_cat, form_login=form_login, form_register=form_register)
# delete category from database
@categories.route('/categories/<int:category_id>/delete', methods=['GET','POST'])
@login_required
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    flash('The category has been deleted!', 'success')
    return redirect(url_for('categories.all_categories'))
    
# display all books from the category    
@categories.route('/category/<string:Name>')
def category_books(Name):
    form_login = LoginForm()
    form_register = RegisterForm()
    page = request.args.get('page', 1, type=int)
    category_query = Category.query.filter_by(Name=Name).first_or_404()
    books = Book.query.filter_by(category=category_query).order_by(Book.isbn.desc()).paginate(page=page, per_page=6)
    return render_template('category/category_books.html',books=books, category=category_query, form_login=form_login, form_register=form_register)