from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class AddPetForm(FlaskForm):
    '''form to add a pet'''
    name = StringField('Pet Name', validators=[InputRequired(message='Name is required')])
    species = SelectField('Species', choices = [('cat', 'cat'), ('dog', 'dog'), ('porcupine', 'porcupine')], validators=[InputRequired(message='Species is required')])
    photo_url = StringField('Photo Url', validators=[Optional(), URL(message='Please enter a valid URL')])
    age = IntegerField('Age', validators=[Optional(), NumberRange(min=0, max=30, message='Age must be between 0 & 30')])
    notes = TextAreaField('Notes', validators=[Optional()])

class EditPetForm(FlaskForm):
    '''form to edit a pet'''
    notes = TextAreaField('Notes', validators=[Optional()])
    photo_url = StringField('Photo Url', validators=[Optional(), URL(message='Please enter a valid URL')])
    available = BooleanField('Available?', default='checked', false_values=(False, 'false', 'f'))