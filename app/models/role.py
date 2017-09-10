from app import db
from app.models import DB_Base
from flask import abort


class Role(db.Model, DB_Base):
    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    users = db.relationship("User", backref="role", lazy="dynamic")

    @staticmethod
    def get_all_items():
        roles = Role.query.all()
        if roles is None:
            abort(404)
        return roles

    @staticmethod
    def get_item_by_id(id):
        role = Role.query.get(id)
        if role is None:
            abort(404)
        return role
