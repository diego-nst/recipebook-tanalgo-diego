from django.urls import path
from .views import recipe_list, recipe, RecipeDetailView, RecipeListView

urlpatterns = [
    path('',RecipeListView.as_view(),name='recipe-list'),
    path('recipes/list', RecipeListView.as_view(), name='recipe-list'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe'),
]

app_name = 'ledger'