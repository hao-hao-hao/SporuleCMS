from app import db
from flask import abort


class Category(db.Model):
    _tablename_ = "category"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    posts = db.relationship("Post", backref="category", lazy="dynamic")

    @staticmethod
    def get_all_items():
        categories = Category.query.all()
        return categories

    @staticmethod
    def get_item_by_id(id):
        category = Category.query.get(id)
        if category is None:
            abort(404)
        return category

    def add_itself(self):
        db.session.add(self)
        db.session.commit()

    def delete_itself(self):
        db.session.delete(self)
        db.session.commit()

