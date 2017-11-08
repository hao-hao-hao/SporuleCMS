from app import db
from app.modules.front_end import front_end
from app.models import Post, Tag, Category
from flask import render_template
from datetime import datetime


@front_end.route("/")
@front_end.route("/<int:page>")
def home(page=1):
    posts = Post.get_all_items_pagination(page=page)
    return render_template('home.html', posts=posts)


@front_end.route("/tags/<tag_name>")
def tag(tag_name):
    posts = Tag.get_item_by_name(tag_name).posts.filter(
        Post.post_date <= datetime.now()).order_by(db.desc(Post.post_date)).paginate(1, 10, True)
    return render_template('home.html', posts=posts, title='Tag: ' + tag_name)


@front_end.route("/category/<category_name>")
def category(category_name):
    posts = Category.get_item_by_name(
        category_name).posts.filter(Post.post_date <= datetime.now()).order_by(db.desc(Post.post_date)).paginate(1, 10, True)
    return render_template('home.html', posts=posts, title='Category: ' + category_name)
