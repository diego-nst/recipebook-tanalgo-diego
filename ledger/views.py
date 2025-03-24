from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .models import Recipe, RecipeImage
from.forms import RecipeImageForm, RecipeForm


class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/recipe_list.html'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'ledger/recipe.html'
    redirect_field_name = 'URL'


class ImageCreateView(CreateView, LoginRequiredMixin):
    model = RecipeImage
    fields = '__all__'
    template_name = 'ledger/recipe_add.html'
    form = RecipeImageForm
    def get_success_url(self):
        return reverse_lazy('ledger:recipe', kwargs={ 'pk': self.object.pk })
    

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = '__all__'
    template_name = 'ledger/recipe_add.html'
    form = RecipeForm
    def get_success_url(self):
        return reverse_lazy('ledger:recipe', kwargs={ 'pk': self.object.pk })


def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {"recipes": recipes}
    return render(request, 'ledger/recipe_list.html', ctx)


def recipe(request, pk):
    ctx = {"recipe": Recipe.objects.get(pk=pk)}
    return render(request, 'ledger/recipe.html', ctx)
