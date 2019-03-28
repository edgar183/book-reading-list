from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from app.models import Category

class Add_Category(FlaskForm):
    Name = StringField('Category Name', validators=[DataRequired()])
    submit = SubmitField('Add')
    
    def validate_Name(self, Name):
        category = Category.query.filter_by(Name=Name.data).first()
        if category:
            raise ValidationError('The category alredy exists.')