from flask import render_template, flash, request, redirect, url_for
from flask_login import login_user, current_user, login_required
from app import admin_permission
from app.models import Tag
from .. import admin
from ..forms import Edit_Tag_Form

@admin.route("/tags/")
@admin_permission.require(http_exception=403)
@login_required
def all_tags():
    tags = Tag.get_all_items()
    return render_template("all_tags.html", tags = tags, title="All Tags")


@admin.route("/tags/<tag_id>/edit/", methods=["GET", "POST"])
@login_required
def edit_tag(tag_id=1):
    tag = Tag.get_item_by_id(tag_id)
    form = Edit_Tag_Form()
    form.load_object_to_form(tag)
    if form.load_form_to_object(tag):
        return redirect(url_for("admin.all_tags"))
    return render_template("edit_tag.html", form=form)
