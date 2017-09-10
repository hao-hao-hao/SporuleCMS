from app import create_app
from app import db
from app.models import Role, User
from random import randint

if __name__ == "__main__":
    app = create_app("config.development")  # start app with config
    with app.app_context():
        db.drop_all()
        db.create_all()
        admin = Role(name="admin")
        #set up intial user
        admin_user = User.create_user("Sporule", "hao@sporule.com","12345678",1)
        db.session.add(admin)
        db.session.add(admin_user)
        db.session.commit()
