from app import ma
from models import *


class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "age", "phone")


class CategorySchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "user_id")


class ItemSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "description", "category_id")