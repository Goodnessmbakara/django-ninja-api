from ninja import ModelSchema, Schema
from pydantic import BaseModel

from inventory.models import Product


class CategorySchema(Schema):
    name: str
    slug: str

class ProductSchema(BaseModel):
    name: str
    web_id: str
    category: int


class SignInSchema(BaseModel):
    email: str
    password: str