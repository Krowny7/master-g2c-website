from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, EmailField, PasswordField, TelField
from wtforms.validators import DataRequired, Email, Length

class ApplicationForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(max=100)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(max=100)])
    email = EmailField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    phone = TelField('Phone Number', validators=[Length(max=20)])
    education = TextAreaField('Education Background')
    motivation = TextAreaField('Motivation Letter', validators=[DataRequired()])
    cv = FileField('CV (PDF)')

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    email = EmailField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    subject = StringField('Subject', validators=[DataRequired(), Length(max=200)])
    message = TextAreaField('Message', validators=[DataRequired()])
