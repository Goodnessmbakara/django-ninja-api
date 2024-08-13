from typing import List, Optional

from django.shortcuts import get_object_or_404
from ninja import NinjaAPI

from api.models import BlogPost
from api.schemas import NotFoundSchema, PostCreate, PostOut, PostUpdate

api = NinjaAPI()


@api.get("/posts", response=List[PostOut])
def posts(request, title: Optional[str] = None):
    if title:
        return Track.objects.filter(title__icontains=title)
    return BlogPost.objects.all()
 
@api.get("/posts/{post_id}", response={200: PostOut, 404: NotFoundSchema})
def posts(request, post_id):
    return get_object_or_404(BlogPost, pk=post_id)

