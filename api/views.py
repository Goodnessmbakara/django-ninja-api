from ninja import NinjaAPI, Router
from typing import List
from django.shortcuts import get_object_or_404
from django.conf import settings
from .models import Post
from .schemas import PostCreate, PostUpdate, PostOut

# # Define JWT authentication using Django-Ninja
# class JWTAuth(JWTBearer):
#     def authenticate(self, request):
#         user = super().authenticate(request)
#         return user

api = NinjaAPI(title="Blog API", version="1.0.0", auth=JWTAuth(), csrf=False)

# Define the blog router
blog_router = Router()

@blog_router.post("/", response=PostOut)
def create_post(request, data: PostCreate):
    user = request.user
    post = Post.objects.create(
        title=data.title,
        content=data.content,
        author=user
    )
    return post

@blog_router.get("/", response=List[PostOut])
def list_posts(request):
    return Post.objects.all()

@blog_router.get("/{post_id}", response=PostOut)
def get_post(request, post_id: int):
    post = get_object_or_404(Post, id=post_id)
    return post

@blog_router.put("/{post_id}", response=PostOut)
def update_post(request, post_id: int, data: PostUpdate):
    post = get_object_or_404(Post, id=post_id)
    if data.title is not None:
        post.title = data.title
    if data.content is not None:
        post.content = data.content
    post.save()
    return post

@blog_router.delete("/{post_id}", response=None)
def delete_post(request, post_id: int):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return None

# Define auth router for authentication endpoints
auth_router = Router()

@auth_router.post("/token/")
def token_obtain_pair(request):
    return api.auth.get_token_pair(request)

@auth_router.post("/token/refresh/")
def token_refresh(request):
    return api.auth.refresh_token(request)

# Add routers to the API
api.add_router("/posts/", blog_router)
api.add_router("/auth/", auth_router)
