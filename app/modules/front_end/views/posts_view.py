from app.modules.front_end import front_end
from app.models import Post
from flask_login import current_user
from flask_principal import Identity


@front_end.route("/post/<int:post_id>/<slug>")
def post(post_id, slug):
    return Post.get_item_by_id(post_id).title
