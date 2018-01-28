import re
from flask import url_for, redirect, request
from flask_principal import UserNeed, RoleNeed
from flask_migrate import Migrate


class Helper():
    @staticmethod
    def is_None(obj):
        return obj is None

    @staticmethod
    def slugify(strings, separator="-", to_lower=True):
        # use regex to replace all the special character to '-'
        strings = re.sub("[^a-zA-Z0-9\n\.]", separator, strings)
        if to_lower:
            strings = strings.lower()
        return strings

    @staticmethod
    def register_error_handler(app):
        """
        Error handlers
        """
        @app.errorhandler(403)
        def permission_denied(e):
            # redirect to login page, set next parameter to the original page.
            return redirect(url_for("admin.login", next=request.url))

        @app.errorhandler(404)
        def page_not_found(e):
            return redirect(url_for("front_end.home", next=request.url))

    @staticmethod
    def registetr_blueprints(app):
        from app.modules.admin import admin
        app.register_blueprint(admin, url_prefix='/admin')
        from app.modules.front_end import front_end
        app.register_blueprint(front_end)

    @staticmethod
    def register_context_processor(app):
        """
        Inject objects as global template objects
        """

        @app.context_processor
        def inject_navigation():
            """Inject navigation into econtext_processor
            """
            from app.models import Navigation
            navigations = Navigation.genenrate_navigation_list(
                Navigation.get_all_items())
            return dict(navigations=navigations)

        @app.context_processor
        def inject_category():
            """Inject categories into context_processor
            """
            from app.models import Category
            categories = Category.get_all_items()
            return dict(categories=categories)

        @app.context_processor
        def inject_collection():
            """Inject collections into context_processor
            """
            from app.models import Tag
            collections = Tag.get_all_collections()
            return dict(collections=collections)

    @staticmethod
    def initial_extensions(app, db, login_manager, principals, bcrypt):
        """initialize 3rd party exntesions
        """
        db.init_app(app)
        Migrate(app, db)
        # set default redirect login page
        login_manager.login_view = "admin.login"
        login_manager.init_app(app)
        principals.init_app(app)
        bcrypt.init_app(app)
