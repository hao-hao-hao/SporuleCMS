from flask_wtf import Form
from flask import request
from app import db


class Super_Form(Form):
    """#preload object to the form if is a "GET" Request
    """

    def load_object_to_form(self, obj):
        """ fill object to the form if is a GET request
        """
        if request.method == "GET":
            fields = list(self.data.keys())
            for field in fields:
                self[field].data = getattr(obj, field)
            return True
        else:
            return False

    def load_form_to_object(self, obj, query=""):
        """convert form into object if is a POST request
        """
        if request.method == "POST" and self.validate_on_submit():
            fields = list(self.data.keys())
            for field in fields:
                setattr(obj, field, self[field].data)
            if query == "password":
                obj.hash_password()
            if query == 'tags':
                obj.generate_tags()
            db.session.commit()
            return True
        else:
            return False

    @staticmethod
    def get_chocies_data(objs, default=(-1, "Default Choice")):
        choices = default
        choices += [(obj.id, obj.name) for obj in objs]
        return choices
