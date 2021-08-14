from app.views import index
from django.urls import path

from app.views import create, edit, delete_recipe, details

urlpatterns = (
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('edit/:id', edit, name='edit'),
    path('delete/:id', delete_recipe, name='delete'),
    path('details/:id', details, name='details'),
)