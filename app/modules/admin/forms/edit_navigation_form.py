from app.forms import Super_Form
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired

class Edit_Navigation_Form(Super_Form):
    name = StringField("Name", validators=[DataRequired()])
    link = StringField("Link")
    parent_id = SelectField("Parent", coerce=int)