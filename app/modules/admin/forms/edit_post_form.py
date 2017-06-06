from app.forms import Super_Form
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired

class Edit_Post_Form(Super_Form):
    title = StringField("Title", validators=[DataRequired()])
    content = TextAreaField("Content", validators=[DataRequired()])
    category_id = SelectField("Category", coerce=int)