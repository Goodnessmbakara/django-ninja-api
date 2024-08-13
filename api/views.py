from typing import List

from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404
from ninja import Router
from ninja.security import django_auth
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .models import BlogPost
from .schemas import BlogPostOutSchema, BlogPostSchema

User = get_user_model()

blog_router = Router()

auth_router = Router()

@auth_router.post("/token/")
def token_obtain_pair(request):
    return TokenObtainPairView.as_view()(request._request)

@auth_router.post("/token/refresh/")
def token_refresh(request):
    return TokenRefreshView.as_view()(request._request)

@blog_router.post("/", response=BlogPostOutSchema, auth=django_auth)
def create_post(request, data: BlogPostSchema):
    post = BlogPost.objects.create(**data.dict(), author=request.user)
    return post

@blog_router.get("/{post_id}", response=BlogPostOutSchema)
def get_post(request, post_id: int):
    post = get_object_or_404(BlogPost, id=post_id)
    return post

@blog_router.put("/{post_id}", response=BlogPostOutSchema, auth=django_auth)
def update_post(request, post_id: int, data: BlogPostSchema):
    post = get_object_or_404(BlogPost, id=post_id, author=request.user)
    for attr, value in data.dict().items():
        setattr(post, attr, value)
    post.save()
    return post

@blog_router.delete("/{post_id}", auth=django_auth)
def delete_post(request, post_id: int):
    post = get_object_or_404(BlogPost, id=post_id, author=request.user)
    post.delete()
    return {"success": True}

@blog_router.get("/", response=List[BlogPostOutSchema])
def list_posts(request, title: str = None, page: int = 1, per_page: int = 10):
    posts = BlogPost.objects.all()
    if title:
        posts = posts.filter(Q(title__icontains=title))
    paginator = Paginator(posts, per_page)
    return paginator.page(page).object_list