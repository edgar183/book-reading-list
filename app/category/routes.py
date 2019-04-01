"""
    Routes to handel category object in database
    By adding, editing, deleting and displaying 
    list of all publishers from database.
"""
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_required
from app import  db
from app.models import Category, Book
from app.category.forms import Add_Category

categories = Blueprint('categories', __name__, url_prefix='/category')

# display list of categories
@categories.route('/categories')
def all_categories():
    categories = Category.query.all()
    return render_template('category/categories.html', categories=categories, title='Categories')
    
# individual category route
@categories.route('/categories/<int:category_id>')
@login_required
def category(category_id):
    category = Category.query.get_or_404(category_id)
    return render_template('category/category.html', title=category.Name, category=category)

# add category     
@categories.route('/categories/add', methods=['GET','POST'])
@login_required
def add_category():
    form = Add_Category()
    if form.validate_on_submit():
        category = Category(Name=form.Name.data)
        db.session.add(category)
        db.session.commit()
        flash('New Category has been added!', 'success')
        return redirect(url_for('categories.all_categories'))
    return render_template('category/add_category.html', title='New Category', form=form, legend='Add New Category')

# edit category name
@categories.route('/categories/<int:category_id>/edit', methods=['GET','POST'])
@login_required
def edit_category(category_id):
    category = Category.query.get_or_404(category_id)
    form = Add_Category()
    if form.validate_on_submit():
        category.Name = form.Name.data
        db.session.commit()
        flash('The category name has been updated!', 'success')
        return redirect(url_for('categories.all_categories', category_id=category.CategoryId))
    elif request.method == 'GET': 
        form.Name.data = category.Name
    return render_template('category/add_category.html', title='Edit Category ', form=form, legend='Edit Category Name')

# delete category from database
@categories.route('/categories/<int:category_id>/delete', methods=['POST'])
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
    page = request.args.get('page', 1, type=int)
    category_query = Category.query.filter_by(Name=Name).first_or_404()
    books = Book.query.filter_by(category=category_query).order_by(Book.isbn.desc()).paginate(page=page, per_page=6)
    return render_template('category/category_books.html',books=books, category=category_query)