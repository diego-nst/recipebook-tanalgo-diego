from django.urls import path
from .views import RecipeDetailView, RecipeListView, ImageCreateView, RecipeCreateView

urlpatterns = [
    path('',RecipeListView.as_view(),name='recipe-list'),
    path('recipes/list', RecipeListView.as_view(), name='recipe-list'),
    path('recipe/add', RecipeCreateView.as_view(), name='recipe-add'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe'),
]

app_name = 'ledger'