from app import db, login_manager, bcrypt
from flask import session, current_app, abort
from app.models import Post, DB_Base
from flask_login import current_user, login_user, logout_user
from flask_principal import Identity, AnonymousIdentity, identity_changed


class User(db.Model, DB_Base):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    posts = db.relationship("Post", backref="user", lazy="dynamic")
    role_id = db.Column(db.Integer, db.ForeignKey("role.id"))

    # create new user
    @staticmethod
    def create_user(name, email, password, role_id=2):
        password = bcrypt.generate_password_hash(password)
        user = User(name=name, email=email, password=password, role_id=role_id)
        return user

    def hash_password(self):
        self.password = bcrypt.generate_password_hash(self.password)

    def is_owner_or_admin(self, post_id):
        post = Post.get_item_by_id(post_id)
        if post.user_id == self.id or self.is_admin():
            return True
        else:
            return False

    # register self to database
    def register_self(self):
        # load user from the database
        user = User.get_user_by_email(self.email)
        # check if user is already in database
        if user is None:
            self.role_id = 2
            DB_Base.add_itself(self)
            return True
        else:
            return False

    # get all the users
    @staticmethod
    def verify_credentials(email, password):
        user = User.get_user_by_email(email)
        # return user if email and password is matched
        if user is not None:
            if bcrypt.check_password_hash(user.password, password):
                return user
        return None

    # get all the users
    @staticmethod
    def get_all_items():
        return User.query.all()

    # get user by user id.
    @staticmethod
    def get_item_by_id(id):
        user = User.query.get(id)
        if user is None:
            abort(404)
        return user

    # get user by email address
    @staticmethod
    def get_user_by_email(email):
        return User.query.filter_by(email=email).first()

    # property for flask-login
    @property
    def is_authenticated(self):
        return True
    # property for flask-login

    @property
    def is_active(self):
        return True
    # property for flask-login

    @property
    def is_anonymous(self):
        return False

    # method for flask-login
    def get_id(self):
        return str(self.id)

    # flask login manager userl loader
    @login_manager.user_loader
    def load_user(id):
        return User.get_item_by_id(id)

    # check if current user is admin
    def is_admin(self):
        return self.role.name == "admin"

    # method for login itself
    def login(self, remember_me):
        # login user in Flask Login, user will be stored to current_user
        login_user(self, remember_me)
        # send user into Flask Principle to notify the identity change
        identity_changed.send(current_app._get_current_object(), identity=Identity(self.id))

    # method for logout itself
    @staticmethod
    def logout():
        if current_user is not None:
            # remove sessions set by Flask Login
            logout_user()
            # remove sessions set by Flask Princple
            for key in ('identity.name', 'identity.auth_type'):
                session.pop(key, None)
            # let flask princple know the user is logout
            identity_changed.send(
                current_app._get_current_object(), identity=AnonymousIdentity())
