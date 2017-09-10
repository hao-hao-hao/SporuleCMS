from flask import Flask
from app.helpers import Helper
from flask_login import LoginManager, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_principal import Principal, Permission, RoleNeed, UserNeed, identity_loaded
from flask_bcrypt import Bcrypt

"""
Create extensions instance
"""
# Create SQLAlchemy instance
db = SQLAlchemy()
# Create Flask Login Manager instance(Login Management)
login_manager = LoginManager()
# create Flask Principal (Role Management)
principals = Principal()
# set admin permission
admin_permission = Permission(RoleNeed("admin"))
# create Bcrypt(for hash password)
bcrypt = Bcrypt()


def create_app(configObject):
    """
    Initiate the flask app instance
    """
    # Create flask application instance
    app = Flask(__name__)

    # Load config profile
    app.config.from_object(configObject)
    # register blueprints
    Helper.registetr_blueprints(app)
    # initial 3rd party extensions
    Helper.initial_extensions(app, db, login_manager, principals, bcrypt)
    # register global context processor
    Helper.register_context_processor(app)
    # register http error handler
    Helper.register_error_handler(app)

    @identity_loaded.connect_via(app)
    def on_identity_loaded(sender, identity):
        """
        Load user roles and id to identity for permission management (part of the flask_principal)
        """
        # set the identity user to current login user
        identity.user = current_user
        if current_user.is_anonymous is not True:
            # add user id to identity
            identity.provides.add(UserNeed(current_user.id))
            # add user role  to identity
            identity.provides.add(RoleNeed(current_user.role.name))

    # return app object
    return app
