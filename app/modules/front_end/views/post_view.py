from app.modules.front_end import front_end
from app.models import Post
from flask import render_template
from flask_login import current_user
from flask_principal import Identity

@front_end.route("/post/<int:post_id>/")
@front_end.route("/post/<int:post_id>/<slug>")
def post(post_id, slug=''):
    post = Post.get_item_by_id(post_id)
    return render_template('post.html', post=post)
