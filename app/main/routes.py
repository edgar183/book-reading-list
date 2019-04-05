from flask import render_template, request, Blueprint
from app.models import Book
from app import app

main = Blueprint('main', __name__)

# home page
@main.route('/')
@main.route('/index')
def index():
    page = request.args.get('page', 1, type=int)
    books = Book.query.order_by(Book.isbn.desc()).paginate(page=page, per_page=6)
    return render_template('index.html',books=books)
    

    