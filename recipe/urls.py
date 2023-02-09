from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('tag/<int:tag_id>/', index, name='tag_view'),
    path('category/<str:category_slug>/', index, name='category_view'),
    path('recipe/<str:recipe_slug>/', recipe_view, name='recipe_view'),
    path('about/', about, name='about'),
    path('add_recipe/', add_recipe, name='add_recipe'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('search/', Search.as_view(), name='search')
]

