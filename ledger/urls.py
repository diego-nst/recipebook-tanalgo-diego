from django.urls import path
from .views import recipe_list, recipe1, recipe2

urlpatterns = [
    path('',recipe_list,name='recipe-list'),
    path('recipes/list', recipe_list, name='recipe-list'),
    path('recipe/1', recipe1, name='recipe1'),
    path('recipe/2', recipe2, name='recipe2'),
]

app_name = 'ledger'