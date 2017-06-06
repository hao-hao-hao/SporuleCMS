from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class Register_Form(Form):
    name = StringField("Nick Name")
    email = StringField("Email Address", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])