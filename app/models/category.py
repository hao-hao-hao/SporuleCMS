from app import db
from app.models import DB_Base
from flask import abort


class Category(db.Model, DB_Base):
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
