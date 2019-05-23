from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from app.models import Publisher

class Add_Publisher(FlaskForm):
    publisherName = StringField('Publisher Name', validators=[DataRequired()])
    submit = SubmitField('Add')
    
    def validate_Name(self, Name):
        publisher = Publisher.query.filter_by(Name=Name.data).first()
        if publisher:
            raise ValidationError('The Publisher alredy exists.')