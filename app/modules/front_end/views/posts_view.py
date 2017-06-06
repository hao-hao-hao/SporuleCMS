from app.modules.front_end import front_end
from app.models import Post
from flask_login import current_user
from flask_principal import Identity


@front_end.route("/")
def all_posts():
    # return all posts if use is admin.
    return Post.get_all_items()[0].title


@front_end.route("/post/<int:post_id>/")
def post(post_id):
    return Post.get_item_by_id(post_id).title
