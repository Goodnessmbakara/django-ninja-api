from ninja import ModelSchema, Schema
from pydantic import BaseModel

from inventory.models import Product


class CategorySchema(Schema):
    class Config:
        orm_mode = True
    name: str
    slug: str

class ProductSchema(BaseModel):
    class Config:
        orm_mode = True
    name: str
    web_id: str
    category: int


class SignInSchema(BaseModel):
    email: str
    password: str

class ProductResponseSchema(Schema):
    name: str
    category: CategorySchema