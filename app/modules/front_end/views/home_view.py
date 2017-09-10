from app.modules.front_end import front_end
from app.models import Post, Tag
from flask import render_template
from flask_login import current_user
from flask_principal import Identity


@front_end.route("/")
@front_end.route("/<int:page>")
def home(page=1):
    posts = Post.get_all_items_pagination(page=page)
    return render_template('home.html', posts=posts)
