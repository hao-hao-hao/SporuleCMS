from flask_login import current_user, login_required
from flask import render_template, abort, redirect, url_for, request, session
from app.models import Post, Category
from .. import admin
from ..forms import Edit_Post_Form


@admin.route("/posts/")
@login_required
def all_posts():
    posts = current_user.posts
    # return all posts if user is admin.
    if current_user.is_admin():
        posts = Post.get_all_items()
    return render_template("all_posts.html", posts=posts)


@admin.route("/posts/new/", methods=["GET", "POST"])
@login_required
def new_post():
    form = Edit_Post_Form()
    post = Post()
    form.category_id.choices = [(category.id, category.name)
                                for category in Category.get_all_items()]
    if form.load_form_to_object(post, query="post"):
        post.add_itself()
        return redirect(post.url())
    return render_template("edit_post.html", form=form)


@admin.route("/posts/<post_id>/delete/", methods=["GET", "POST"])
@login_required
def delete_post(post_id):
    post = Post.get_item_by_id(post_id)
    post.delete_itself()
    return redirect(url_for("admin.all_posts"))


@admin.route("/posts/<post_id>/edit/", methods=["GET", "POST"])
@login_required
def edit_post(post_id):
    if current_user.is_owner_or_admin(post_id):
        form = Edit_Post_Form()
        post = Post.get_item_by_id(post_id)
        form.category_id.choices = [(category.id, category.name)
                                    for category in Category.get_all_items()]
        post.tags_temp = ','.join(t.name for t in post.tags)
        form.load_object_to_form(post)
        if form.load_form_to_object(post, query='post'):
            return redirect(post.url())
        return render_template("edit_post.html", form=form)
    else:
        # raise 403 Forbidden for insuficcient permissions
        abort(403)
