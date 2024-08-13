from django.urls import path
from ninja import NinjaAPI
from .views import auth_router, blog_router

api = NinjaAPI(title="Blog API", version="1.0.0", auth=JWTAuth(), csrf=False)
api.add_router("/posts/", blog_router)
api.add_router("/auth/", auth_router)

urlpatterns = [
    path('', api.urls),
]
