from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class MessageForm(FlaskForm):
    message = StringField('Enter your school list')
    submit = SubmitField('Send')


  
    