from django.urls import path
from .views import recipe_list, recipe1, recipe2, RecipeDetailView, RecipeListView

urlpatterns = [
    path('',recipe_list,name='recipe-list'),
    path('recipes/list', RecipeListView.as_view(), name='recipe-list'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe'),
]

app_name = 'ledger'