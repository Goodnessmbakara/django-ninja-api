from typing import List, Optional

from django.contrib.auth import authenticate, get_user_model, login, logout
from django.forms.models import model_to_dict
from django.middleware.csrf import get_token
from django.shortcuts import get_object_or_404
from ninja import NinjaAPI
from ninja.security import HttpBasicAuth, django_auth

from api import schemas
from api.schemas import CategorySchema, ProductSchema
from inventory.models import Category, Product

User = get_user_model()

api = NinjaAPI()

class BasicAuth(HttpBasicAuth):
    def authenticate(self, request, username, password):
        user = authenticate(request, username=username, password=password)
        return user
    
@api.post("/inventory/category", auth=BasicAuth())
def post_category(request, data: CategorySchema):
    qs = Category.objects.create(**data.dict())
    return {"name": qs.name}

@api.post("/inventory/product", auth=BasicAuth())
def post_product(request, data: ProductSchema):
    data = data.dict()
    category_id = data.pop("category")
    category = get_object_or_404(Category, pk=category_id)
    product = Product(**data)
    product.category = category
    product.save()
    return {"name": product.name, "category": product.category.name}

@api.get("/inventory/category/all", response=List[CategorySchema])
def get_category_list(request):
    qs = Category.objects.all()
    return qs
 
@api.get("/inventory/product/category/{category_slug}", response=List[ProductSchema],auth=BasicAuth())
def get_product_by_category(request, category_slug: str):
    qs = Product.objects.filter(category__slug=category_slug)
    return qs

@api.put("/inventory/category/{category_id}", response=List[CategorySchema],auth=BasicAuth())
def update_category(request, category_id: int, payload: CategorySchema):
    category = get_object_or_404(Category, id=category_id)
    for attr,value in payload.dict().items():
        if value:
            setattr(category, attr,value)
    category.save()
    return {"Success":True}

@api.delete("/inventory/category/{cat_id}",auth=BasicAuth())
def delete_category(request, cat_id: int, payload: CategorySchema):
    category = get_object_or_404(Category, id=cat_id)
    category.delete()
    return {"Success":True}

@api.get("/set-csrf-token")
def get_csrf_token(request):
    return {"csrftoken": get_token(request)}


@api.post("/login")
def login_view(request, payload: schemas.SignInSchema):
    user = authenticate(request, username=payload.email, password=payload.password)
    if user is not None:
        login(request, user)
        return {"message":"success","session_id":request.session.session_key}
    return {"success": False, "message": "Invalid credentials"}


@api.post("/logout", auth=BasicAuth())
def logout_view(request):
    logout(request)
    return {"message": "Logged out"}


@api.get("/user", auth=BasicAuth())
def user(request):
    secret_fact = (
        "The moment one gives close attention to any thing, even a blade of grass",
        "it becomes a mysterious, awesome, indescribably magnificent world in itself."
    )
    return {
        "username": request.user.username,
        "email": request.user.email,
        "secret_fact": secret_fact
    }


@api.post("/register")
def register(request, payload: schemas.SignInSchema):
    try:
        User.objects.create_user(username=payload.email, email=payload.email, password=payload.password)
        return {"success": "User registered successfully"}
    except Exception as e:
        return {"error": str(e)}