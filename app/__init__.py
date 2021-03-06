from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from app.config import Config


# init app
app = Flask(__name__)
app.config.from_object(Config)

# init DB in app
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

from app.main.routes import main
from app.user.routes import users
from app.author.routes import authors
from app.publisher.routes import publishers
from app.category.routes import categories
from app.book.routes import books
from app.reading_list.routes import readinglists

app.register_blueprint(main)
app.register_blueprint(users)
app.register_blueprint(authors)
app.register_blueprint(publishers)
app.register_blueprint(categories)
app.register_blueprint(books)
app.register_blueprint(readinglists)

