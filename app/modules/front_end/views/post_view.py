from app.modules.front_end import front_end
from app.models import Post
from flask import render_template, abort
from datetime import datetime


@front_end.route("/post/<int:post_id>/")
@front_end.route("/post/<int:post_id>/<slug>")
def post(post_id, slug=''):
    post = Post.get_item_by_id(post_id)
    if(post.post_date <= datetime.now()):
        return render_template('post.html', post=post, title=post.title)
    abort(404)
