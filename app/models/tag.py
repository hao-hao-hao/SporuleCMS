from app import db
from app.models import DB_Base
from app.decorators import links


class Tag(db.Model, DB_Base):
    _tablename_ = "tag"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    is_collection = db.Column(db.Boolean, nullable=True)

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

    @links.permalink
    # generate the front end view url for this post
    def url(self):
        return "front_end.tag", {"tag_name":self.name}
