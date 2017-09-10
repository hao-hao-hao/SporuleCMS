from app import create_app
from app import db
from app.models import Role, User, Post
from random import randint

if __name__ == "__main__":
    app = create_app("config.development")  # start app with config
    app.run(host='0.0.0.0')
