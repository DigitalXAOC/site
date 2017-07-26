from flask_wtf import FlaskForm, RecaptchaField
from wtforms import TextField, BooleanField, PasswordField
from wtforms.validators import Required

class LoginForm(FlaskForm):
    email = TextField('email', validators = [Required()])
    password = PasswordField('password')
    remember_me = BooleanField('remember_me', default = False)