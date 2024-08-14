from typing import List, Optional

from django.shortcuts import get_object_or_404
from ninja import NinjaAPI

from inventory.models import Category, Product
from api.schemas import CategoryIn, ProductSchema

api = NinjaAPI()

@api.post("/inventory/category")
def post_category(request, data: CategoryIn):
    qs = Category.objects.create(**data.dict())
    return {"name": qs.name}

@api.get("/inventory/product", response=List[PostOut])
def post_product(request, data: ProductSchema):
    qs = Product.objects.create(**data.dict())
    return {"name": qs.name}

 