from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired


class Register_Form(Form):
    name = StringField("Nick Name")
    email = StringField("Email Address", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
