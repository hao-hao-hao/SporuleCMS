from app import db


class DB_Base():
    """
    This is a base class for basic DB operations
    """

    @staticmethod
    def add_itself(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def delete_itself(self):
        db.session.delete(self)
        db.session.commit()
