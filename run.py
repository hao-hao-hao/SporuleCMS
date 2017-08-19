from app import create_app
from app import db
from app.models import Role, User, Post
from random import randint

if __name__ == "__main__":
    app = create_app("config.development")  # start app with config
#     with app.app_context():
        # db.drop_all()
        # db.create_all()
        # admin = Role(name="admin")
        # author = Role(name="author")
        # db.session.add(admin)
        # db.session.add(author)
        # db.session.commit()
        # for i in range(3):
            # u = User.create_user("User {0}".format(
                # str(i)), "hao{0}@gmail.com".format(str(i)), "1q2w3e4r", 1)
            # b = User.create_user("User {0}{0}".format(
                # str(i)), "hao{0}{0}@gmail.com".format(str(i)), "1q2w3e4r")
            # db.session.add(u)
            # db.session.add(b)
            # db.session.commit()
        # for i in range(30):
            # index = randint(1, 6)
            # p = Post(title="Hello, this is the {0} post".format(str(
                # i)), content="What an amazing Post{0}".format(str(i)), user=User.get_item_by_id(index))
            # db.session.add(p)
#             db.session.commit()
    app.run(host='0.0.0.0')
