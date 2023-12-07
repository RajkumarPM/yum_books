from django.urls import path
from . import views

app_name = 'recipes'  # Change the app_name to 'recipes'

urlpatterns = [
    # /recipes/
    path('', views.index, name='index'),
    # /recipes/id e.g. /recipes/1
    path('<int:recipe_id>/', views.show, name='show'),
    path('create_recipe/', views.create_recipe, name='create'),
    path('<int:recipe_id>/edit_recipe/', views.edit_recipe, name='edit'),
    path('<int:recipe_id>/delete/', views.delete_recipe, name='delete'),
]
