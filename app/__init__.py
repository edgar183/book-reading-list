from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# init app
app = Flask(__name__)
SQLALCHEMY_DATABASE_URI = 'sqlite:///db/bookLibrary.db'
# set up database location config
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/bookLibrary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# init DB in app
db = SQLAlchemy(app)

from app import routes