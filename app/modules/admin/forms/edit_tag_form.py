from app.forms import Super_Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class Edit_Tag_Form(Super_Form):
    name = StringField("Name", validators=[DataRequired()])
    is_collection = BooleanField("Is_Collection")
