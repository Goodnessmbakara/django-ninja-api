from ninja import ModelSchema, Schema
from pydantic import BaseModel

from inventory.models import Product


class CategorySchema(Schema):
    name: str
    slug: str

class ProductSchema(ModelSchema):
    class Config:
        model = Product
        model_fields  = ["name", "web_id", "category"]


class SignInSchema(BaseModel):
    email: str
    password: str