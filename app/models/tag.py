from app import db
from app.models import DB_Base
from flask import abort


class Tag(db.Model, DB_Base):
    _tablename_ = "tag"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    @staticmethod
    def get_all_items():
        tags = Tag.query.all()
        return tags

    @staticmethod
    def get_item_by_id(id):
        tag = Tag.query.get(id)
        return tag

    @staticmethod
    def get_item_by_name(name):
        tag = Tag.query.filter_by(name=name).first()
        return tag
