from flask import render_template, request, Blueprint, url_for
from app.models import Book
from app import app
from app.user.forms import LoginForm, RegisterForm

main = Blueprint('main', __name__)

# home page
@main.route('/')
@main.route('/index')
def index():
    form_login = LoginForm()
    form_register = RegisterForm()
    page = request.args.get('page', 1, type=int)
    books = Book.query.order_by(Book.isbn.desc()).paginate(page=page, per_page=6)
    next_url = url_for('main.index', page=books.next_num) \
        if books.has_next else None
    prev_url = url_for('index', page=books.prev_num) \
        if books.has_prev else None
    return render_template('index.html',books=books, form_login=form_login, form_register=form_register, next_url=next_url,
                           prev_url=prev_url )
    

    