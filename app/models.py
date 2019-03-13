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
author_book = db.Table('author_book', 
            db.Column('AuthorId', db.Integer, db.ForeignKey('author.AuthorId')),
            db.Column('isbn', db.Integer, db.ForeignKey('book.isbn'))
)

book_reading = db.Table('book_reading',
            db.Column('isbn', db.Integer, db.ForeignKey('book.isbn')),
            db.Column('id', db.Integer, db.ForeignKey('lists.id'))
)

# Author Class/Model
class Author(db.Model):
    AuthorId = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(100), nullable=False)
    LastName = db.Column(db.String(100), nullable=False)
    
    def __init__(self, FirstName, LastName):
        self.FirstName = FirstName
        self.LastName = LastName
        
# Publisger Class/Model
class Publisher(db.Model):
    PublisherId = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255), nullable=False)
    book = db.relationship('Book', backref='publisher', lazy=True)
    
    def __init__(self, Name):
        self.Name = Name
        
# Category Class/Model
class Category(db.Model):
    CategoryId = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255), nullable=False)
    book = db.relationship('Book', backref='category', lazy=True)
    
    def __init__(self, Name):
        self.Name = Name
        
# Book Class/Model
class Book(db.Model):
    isbn = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    year = db.Column(db.DateTime, nullable=False, default=datetime.year)
    book_cover = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    publisher_id= db.Column(db.Integer, db.ForeignKey('publisher.PublisherId'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.CategoryId'), nullable=False)
    authors = db.relationship('Author', secondary=author_book, backref=db.backref('writer', lazy='dynamic'))
    readers = db.relationship('Lists', secondary=book_reading, backref=db.backref('reader', lazy='dynamic'))
    
    def __init__(self, title, year, book_cover, description):
        self.title = title
        self.year = year
        self.book_cover = book_cover
        self.description = description
    
# User Class/Model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255),nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    reading_list = db.relationship('Lists', backref='user', lazy=True)
    
    def __init__(self, name,username,password):
        self.name = name    
        self.username = username
        self.password = password
        
    def __repr__(self):
        return '<User %r>' % self.username

#Rading List Class/Model
class Lists(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ListName = db.Column(db.String(255), nullable=False)
    UserId = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __init__(self, ListName):
        self.ListName = ListName
    
