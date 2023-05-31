from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreate, PostUpdate, PostDeleteView


urlpatterns = [
    path("", views.index, name= "index"),

]