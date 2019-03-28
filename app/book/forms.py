from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired
from app.models import Book

class Add_Book(FlaskForm):
    title = StringField('Book Title', validators=[DataRequired()])
    year = StringField('Year Published', validators=[DataRequired()])
    book_cover = StringField('URL link for book cover picture', validators=[DataRequired()])
    description = TextAreaField('Book description ', validators=[DataRequired()])
    publisher = SelectField('Publisher', coerce=int)
    category = SelectField('Category', coerce=int)
    author = SelectField('Author', coerce=int)
    submit = SubmitField('Add')
    


class Add_book_to_readinglit(FlaskForm):
    lists = SelectField('Reading Lists', coerce=int)
    submit = SubmitField('Add')