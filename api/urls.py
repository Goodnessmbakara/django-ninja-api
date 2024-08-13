from django.urls import path
from ninja import NinjaAPI
from .views import blog_router,auth_router

api = NinjaAPI()

api.add_router("/posts/", blog_router)
api.add_router("/auth/", auth_router)

urlpatterns = [
    path("api/v1/", api.urls),
]
