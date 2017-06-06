from flask_login import  login_required
from flask import render_template, abort, redirect, url_for
from app.models import Category
from .. import admin
from ..forms import Edit_Category_Form
from app.helpers import Helper


@admin.route("/categories/")
@login_required
def all_categories():
    categories = Category.get_all_items()
    return render_template("all_categories.html", categories=categories)


@admin.route("/categories/new/", methods=["GET", "POST"])
@login_required
def new_category():
    form = Edit_Category_Form()
    category = Category()
    if form.load_form_to_object(category):
        category.add_itself()
        return redirect(url_for("admin.all_categories"))
    return render_template("edit_category.html", form=form)


@admin.route("/category/<category_id>/delete/", methods=["GET", "POST"])
@login_required
def delete_category(category_id):
    category = Category.get_item_by_id(category_id)
    category.delete_itself()
    return redirect(url_for("admin.all_categories"))


@admin.route("/categories/<category_id>/edit/", methods=["GET", "POST"])
@login_required
def edit_category(category_id):
    form = Edit_Category_Form()
    category = Category.get_item_by_id(category_id)
    if Helper.is_None(category):
        return abort(404)
    form.load_object_to_form(category)
    if form.load_form_to_object(category):
        return redirect(url_for("admin.all_categories"))
    return render_template("edit_category.html", form=form)
