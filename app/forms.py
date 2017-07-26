from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import Required

class LoginForm(FlaskForm):
    email = StringField('Email address', validators = [Required()])
    password = PasswordField('Password')
    remember_me = BooleanField('Remember Me', default = False)
    submit = SubmitField('sign_in')