from app import db


class DB_Base():
    """
    This is a base class for basic DB operations
    """

    def add_itself(self):
        db.session.add(self)
        db.session.commit()

    def delete_itself(self):
        db.session.delete(self)
        db.session.commit()
