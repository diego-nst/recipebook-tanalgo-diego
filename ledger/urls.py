from django.urls import path
from .views import RecipeDetailView, RecipeListView, RecipeCreateView, image_create

urlpatterns = [
    path('',RecipeListView.as_view(),name='recipe-list'),
    path('recipes/list', RecipeListView.as_view(), name='recipe-list'),
    path('recipe/add', RecipeCreateView.as_view(), name='recipe-add'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe'),
    path('recipe/<int:pk>/add_image', image_create, name='image-add'),
]

app_name = 'ledger'