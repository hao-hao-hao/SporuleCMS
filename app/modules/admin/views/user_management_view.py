from flask import render_template,flash, request, redirect, url_for, current_app
from flask_login import login_user, current_user,login_required, logout_user
from app import db, admin_permission
from app.models import User, Role, Post
from .. import admin
from ..forms import Login_Form, Register_Form, Edit_User_Form

@admin.route("/")
@login_required
def admin_home():
    return render_template("admin_base.html",current_user = current_user)

@admin.route("/users/")
@admin_permission.require(http_exception=403)
@login_required
def all_users():
    users = User.get_all_items()
    return render_template("all_users.html",users=users,current_user=current_user,title="All Users")

@admin.route("/users/<user_id>/edit/",methods=["GET","POST"])
@login_required
def edit_user(user_id=1):
    user = current_user
    if user.is_admin():
        user = User.get_item_by_id(user_id)
    form = Edit_User_Form()
    form.role_id.choices=[(role.id,role.name) for role in Role.get_all_items()]
    form.load_object_to_form(user)
    if form.load_form_to_object(user,"password"):
        return redirect(url_for("admin.all_users"))
    return render_template("edit_user.html",form = form)



@admin.route("/register/",methods=["GET","POST"])
def register():
    form = Register_Form()
    if form.validate_on_submit():
        user = User.create_user(form.name.data, form.email.data, form.password.data, role_id = 2)
        if user.register_self():
            flash("Register Successful")
            login_user(user)
            return redirect(request.args.get('next') or url_for("front_end.all_posts"))
    return render_template("register.html",form=form)


@admin.route("/login/",methods=["GET","POST"])
def login():
    #Delete the auto login function before deployment
    if current_app.config["AUTO_LOGIN"]:
        user = User.get_item_by_id(1)
        User.login(user, True)
        return redirect(request.args.get('next') or url_for("front_end.all_posts"))
    #delete the above auto login function before deployment
    form = Login_Form()
    if form.validate_on_submit():
        user = User.verify_credentials(form.email.data,form.password.data)
        if user is not None:
            user.login(form.remember_me.data)
            flash("Login Successful, Welcome {0} !".format(user.name))
            return redirect(request.args.get('next') or url_for("front_end.all_posts"))
    return render_template("login.html",form = form)

@admin.route("/logout/")
@login_required
def logout():
    User.logout()
    return redirect(request.args.get('next') or url_for("front_end.all_posts"))