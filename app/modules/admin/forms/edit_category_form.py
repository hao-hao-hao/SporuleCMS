from app.forms import Super_Form
from wtforms import StringField
from wtforms.validators import DataRequired


class Edit_Category_Form(Super_Form):
    name = StringField("Title", validators=[DataRequired()])
