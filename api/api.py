from typing import List, Optional

from django.shortcuts import get_object_or_404
from ninja import NinjaAPI

from inventory.models import Category, Product
from api.schemas import CategorySchema, ProductSchema

api = NinjaAPI()

@api.post("/inventory/category")
def post_category(request, data: CategorySchema):
    qs = Category.objects.create(**data.dict())
    return {"name": qs.name}

@api.post("/inventory/product")
def post_product(request, data: ProductSchema):
    category_id = data.pop("category_id")
    category = Category.objects.get(pk=category_id)
    qs = Product.objects.create(**data.dict(), category=category)
    return {"name": qs.name}

@api.get("/inventory/category/all", response=List[CategorySchema])
def get_category_list(request):
    qs = Category.objects.all()
    return qs
 
@api.get("/inventory/product/category/{category_slug}", response=List[ProductSchema])
def get_product_by_category(request, category_slug: str):
    qs = Product.objects.filter(category__slug=category_slug)
    #qs = Product.objects.all()
    return qs

@api.put("/inventory/category/{category_id}", response=List[CategorySchema])
def update_category(request, category_id: int, payload: CategorySchema):
    category = get_object_or_404(Category, id=category_id)
    for attr,value in payload.dict().items():
        if value:
            setattr(category, attr,value)
    category.save()
    return {"Success":True}

@api.delete("/inventory/category/{cat_id}")
def delete_category(request, cat_id: int, payload: CategorySchema):
    category = get_object_or_404(Category, id=cat_id)
    category.delete()
    return {"Success":True}