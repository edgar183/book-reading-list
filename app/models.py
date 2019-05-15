"""
    Create database tables by using the SQLAlchamy syntax. 
    This helps to map the tables and columns to classes and objects respectively. The types of the column can be passed as an argument.
"""
from datetime import datetime
from app import db, login_manager
from flask_login import UserMixin


# Callback is used to reload the user object from the user ID stored in the session.
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# many-to-many relationships 
book_reading = db.Table('book_reading',
            db.Column('isbn', db.Integer, db.ForeignKey('book.isbn')),
            db.Column('id', db.Integer, db.ForeignKey('lists.id'))
)

# Author Class/Model
class Author(db.Model):
    AuthorId = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255), nullable=False, unique=True)

# Publisger Class/Model
class Publisher(db.Model):
    PublisherId = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255), nullable=False, unique=True)

# Category Class/Model
class Category(db.Model):
    CategoryId = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255), nullable=False, unique=True)

# Book Class/Model
class Book(db.Model):
    isbn = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    year = db.Column(db.String(4), nullable=False)
    book_cover = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    publisher_id= db.Column(db.Integer, db.ForeignKey('publisher.PublisherId'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.CategoryId'), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.AuthorId'), nullable=False)
    
    author = db.relationship('Author', backref=db.backref('books', lazy='dynamic'))
    category = db.relationship('Category', backref=db.backref('books', lazy='dynamic'))
    publisher = db.relationship('Publisher', backref=db.backref('books', lazy='dynamic'))

# User Class/Model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255),nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    reading_list = db.relationship('Lists', backref='user', lazy='dynamic')

#Rading List Class/Model
class Lists(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ListName = db.Column(db.String(255), nullable=False , unique=True)
    UserId = db.Column(db.Integer, db.ForeignKey('user.id'))
    books_in_list = db.relationship('Book', secondary=book_reading, backref=db.backref('books', lazy='dynamic'))
    
    
