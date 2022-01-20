from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class SchoolForm(FlaskForm):
    message = StringField('Enter your school list')
    submit = SubmitField('Send')

class HomeForm(FlaskForm):
    message = StringField('Enter your home list')
    submit = SubmitField('Send')
  
    