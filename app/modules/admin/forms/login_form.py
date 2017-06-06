from app.forms import Super_Form
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired

class Login_Form(Super_Form):
    email = StringField("Email Address", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me",default=False)