import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://book-admin:boss123@localhost/bookLibrary'
db = SQLAlchemy(app)

meta = db.metadata
engine = db.engine



@app.route('/')
def index():
    return "The home page"
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),debug=True)