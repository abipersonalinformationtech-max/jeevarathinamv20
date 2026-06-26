from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("home2", views.home2, name="home2"),
    path("product2", views.product2, name="product2"),
]
