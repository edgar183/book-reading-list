import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# init app
app = Flask(__name__)
# set up database location config
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://book-admin:boss123@localhost/bookLibrary'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# init DB in app
db = SQLAlchemy(app)
# Author Class/Model
class Author(db.Model):
    AuthorId = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(100))
    LastName = db.Column(db.String(100))
    
    def __init__(self, FirstName, LastName):
        self.FirstName = FirstName
        self.LastName = LastName
        
# Publisger Class/Model
class Publisher(db.Model):
    PublisherId = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255))
    
    def __init__(self, Name):
        self.Name = Name
        
# Category Class/Model
class Category(db.Model):
    CategoryId = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255))
    
    def __init__(self, Name):
        self.Name = Name
    
# User Class/Model
class User(db.Model):
    UserId = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(255))
    userName = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(8), unique=True)
    def __init__(self, Name):
        self.Name = Name    


@app.route('/')
def index():
    return "The home page"
    
#run server
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),debug=True)