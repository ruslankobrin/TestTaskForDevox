from app import db


class Users(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.INTEGER)
    phone = db.Column(db.String(20))

    def __init__(self, *args, **kwargs):
        super(Users, self).__init__(*args, **kwargs)
