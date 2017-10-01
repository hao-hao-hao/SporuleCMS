from app import db
from app.decorators import links
from flask import abort
from flask_login import current_user
from app.helpers import Helper
from app.models import DB_Base
from datetime import datetime


class Post(db.Model, DB_Base):
    _tablename_ = "post"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    post_date = db.Column(db.DateTime)
    edit_date = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"))
    tags = db.relationship('Tag', secondary='post_tag',
                           backref=db.backref("posts", lazy='dynamic'))
    tags_temp = ''

    @staticmethod
    def get_all_items():
        posts = Post.query.all()
        return posts

    @staticmethod
    def get_all_items_pagination(page=1, per_page=10, error_out=True):
        posts = Post.query.order_by(db.desc(Post.post_date)).paginate(
            page, per_page, error_out)
        return posts

    @staticmethod
    def get_item_by_id(id):
        post = Post.query.get(id)
        if post is None:
            abort(404)
        return post

    def add_itself(self, user=current_user):
        if self.post_date is None:
            self.post_date = datetime.now()
        else:
            self.edit_date = datetime.now()
        self.user_id = user.id
        DB_Base.add_itself(self)

    def generate_excerpt(self, length):
        if len(self.content) < length:
            return self.content
        excerpt = self.content[0:length]
        if '<code>' in excerpt and '</code>' not in excerpt:
            excerpt += '</code>'
        return excerpt

    def generate_tags(self):
        self.tags = []
        tags_list = self.tags_temp.split(',')
        from app.models import Tag
        for tag_string in tags_list:
            tag_string_cap = tag_string.strip().title()
            tag = Tag.get_item_by_name(tag_string_cap)
            if tag is None:
                tag = Tag(name=tag_string_cap, is_collection=False)
            self.tags.append(tag)

    # generate slugified title for permanent links
    def slugified_title(self):
        return Helper.slugify(self.title)

    @links.permalink
    # generate the edit url for this post
    def edit_url(self):
        return "admin.edit_post", {"post_id": self.id}

    @links.permalink
    # generate the front end view url for this post
    def url(self):
        return "front_end.post", {"post_id": self.id, "slug": self.slugified_title()}

    @links.permalink_full
    # generate the full url for this post
    def url_full(self):
        return "front_end.post", {'post_id': self.id}
