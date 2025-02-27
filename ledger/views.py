from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Recipe

class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/recipe_list.html'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe.html'

def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {"recipes": recipes}
    return render(request, 'ledger/recipe_list.html', ctx)

def recipe(request, pk):
    ctx = {"recipe": Recipe.objects.get(pk=pk),}
    return render(request, 'recipe.html', ctx)
