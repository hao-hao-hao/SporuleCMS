from wtforms import StringField, SelectField, PasswordField
from wtforms.validators import DataRequired
from app.forms import Super_Form


class Edit_User_Form(Super_Form):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password(Only if you want to change)")
    role_id = SelectField("Role", coerce=int)
