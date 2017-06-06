from flask_login import current_user, login_required
from flask import render_template, abort, redirect, url_for, request
from app.models import User, Post, Role, Navigation
from app import admin_permission, db
from .. import admin
from ..forms import Edit_Navigation_Form
from app.helpers import Helper


@admin.route("/navigations/")
@admin_permission.require(http_exception=403)
@login_required
def all_navigations():
    navs = Navigation.get_all_items()
    return render_template("all_navigations.html",navs = navs)

@admin.route("/navigations/new/",methods=["GET","POST"])
@admin_permission.require(http_exception=403)
@login_required
def new_navigation():
    form = Edit_Navigation_Form()
    navigation = Navigation()
    form.parent_id.choices  = navigation.get_higher_level_navigations()
    if form.load_form_to_object(navigation):
        navigation.add_itself()
        return redirect(url_for("admin.all_navigations"))
    return render_template("edit_navigation.html",form=form)

@admin.route("/navigations/<navigation_id>/edit/",methods=["GET","POST"])
@admin_permission.require(http_exception=403)
@login_required
def edit_navigation(navigation_id):
    form = Edit_Navigation_Form()
    navigation = Navigation.get_item_by_id(navigation_id)
    if Helper.is_None(navigation):
        return abort(404)
    form.parent_id.choices  = navigation.get_higher_level_navigations()
    form.load_object_to_form(navigation)
    if form.load_form_to_object(navigation):
        return redirect(url_for("admin.all_navigations"))
    return render_template("edit_navigation.html",form = form)


@admin.route("/navigations/<navigation_id>/delete/", methods=["GET","POST"])
@admin_permission.require(http_exception=403)
@login_required
def delete_navigation(navigation_id):
    navigation = Navigation.get_item_by_id(navigation_id)
    if not Helper.is_None(navigation):
        navigation.delete_itself()
    return  redirect(url_for("admin.all_navigations"))