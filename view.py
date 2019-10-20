from app import app
from serialise import *
from models import *
from flask import jsonify


@app.route('/')
def hello_world():
    return 'Hello World!!!'


@app.route('/api/users/', methods=['GET'])
def get_users():
    users_schema = UserSchema(many=True)
    all_users = User.query.all()
    # print(type(all_users))
    return jsonify(users_schema.dump(all_users))


@app.route('/api/categories/<id>', methods=['GET'])
def get_category(id):
    categories_schema = CategorySchema(many=True)
    # categories = Category.query.filter(Category.user.id == id)
    categories = Category.query.join(User).filter(User.id == id)
    return jsonify(categories_schema.dump(categories))


@app.route('/api/items/<id>', methods=['GET'])
def get_items(id):
    items_schema = ItemSchema(many=True)
    items = Item.query.join(Category).join(User).filter(User.id == id)
    return jsonify(items_schema.dump(items))