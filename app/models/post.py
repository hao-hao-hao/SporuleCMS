from app import db
from app.decorators import links
from flask import abort
from flask_login import current_user
from app.helpers import helper
from app.models import DB_Base


class Post(db.Model, DB_Base):
    _tablename_ = "post"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"))
    tags = db.relationship('Tag', secondary='post_tag',
                           backref=db.backref("posts", lazy='dynamic'))

    @staticmethod
    def get_all_items():
        posts = Post.query.all()
        return posts

    @staticmethod
    def get_item_by_id(id):
        post = Post.query.get(id)
        if post is None:
            abort(404)
        return post

    def add_itself(self, user=current_user):
        self.user_id = user.id
        DB_Base.add_itself(self)

    def get_author(self):
        from app.models import User
        return User.get_item_by_id(self.user_id)

    # generate slugified title for permanent links
    def slugified_title(self):
        return helper.slugify(self.title)

    @links.permalink
    # generate the edit url for this post
    def edit_url(self):
        return "admin.edit_post", {"post_id": self.id}

    @links.permalink
    # generate the front end view url for this post
    def url(self):
        return "front_end.post", {"post_id": self.id, "slug": self.slugified_title}
