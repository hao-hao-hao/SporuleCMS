from flask import Flask, redirect, url_for, session,request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from flask_principal import Principal, Permission, RoleNeed, UserNeed, identity_loaded
from flask_bcrypt import Bcrypt

#Create SQLAlchemy instance
db = SQLAlchemy()

#Create Flask Login Manager instance
login_manager = LoginManager()
#set default login page
login_manager.login_view = "admin.login"

#create Flask Principal (Role Management)
principals = Principal()
admin_permission = Permission(RoleNeed("admin"))

#create Bcrypt(for hash password)
bcrypt = Bcrypt()


def create_app(configObject):
    #Create flask application instance
    app = Flask(__name__)

    #Load config profile
    app.config.from_object(configObject)
    
    #initialize exntesions

    #Bcrypt
    bcrypt.init_app(app)

    #SQLAlchemy
    db.init_app(app)
    #flask login
    login_manager.init_app(app)
    #flask principle
    principals.init_app(app)
    #method for flask principle
    @identity_loaded.connect_via(app)
    def on_identity_loaded(sender, identity):
        #set the identity user to current login user
        identity.user = current_user
        if current_user.is_anonymous is not True:
            #add user needed to identity
            identity.provides.add(UserNeed(current_user.id))
            #add role  needed to identity
            identity.provides.add(RoleNeed(current_user.role.name))   

    #import  models
    from app import models

    #register blueprints
    from app.modules.admin import admin
    app.register_blueprint(admin,url_prefix='/admin')
    from app.modules.front_end import front_end
    app.register_blueprint(front_end)
    #error handlers
    @app.errorhandler(403)
    def permission_denied(e):
        #redirect to login page, set next parameter to the original page.
        return redirect(url_for("admin.login",next=request.url))
    @app.errorhandler(404)
    def page_not_found(e):
        return redirect(url_for("admin.all_posts",next=request.url))

    #inject navigation as a global template object
    from app.models import Navigation
    @app.context_processor
    def inject_navigation():
        navigations = Navigation.genenrate_navigation_list(Navigation.get_all_items())
        return dict(navigations = navigations)
    #return app object
    return app