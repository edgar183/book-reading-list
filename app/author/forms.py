from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from app.models import Author

class Add_Author(FlaskForm):
    full_name = StringField('Full Name', validators=[DataRequired()])
    submit = SubmitField('Add')

    def validate_full_name(self, full_name):
        author = Author.query.filter_by(full_name=full_name.data).first()
        if author:
            raise ValidationError('The author with this name alredy exists.')