from app import db


class User(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.INTEGER)
    phone = db.Column(db.String(20))

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)


class Category(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship("User", backref="user")

    def __init__(self, *args, **kwargs):
        super(Category, self).__init__(*args, **kwargs)


class Item(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(100))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship("Category", backref="category")

    def __init__(self, *args, **kwargs):
        super(Item, self).__init__(*args, **kwargs)