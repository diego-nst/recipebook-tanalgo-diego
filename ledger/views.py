from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .models import Recipe, RecipeImage
from .forms import RecipeImageForm, RecipeForm


class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/recipe_list.html'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'ledger/recipe.html'
    redirect_field_name = 'URL'


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = '__all__'
    template_name = 'ledger/recipe_add.html'
    form = RecipeForm

    def get_success_url(self):
        return reverse_lazy('ledger:recipe', kwargs={'pk': self.object.pk})


def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {"recipes": recipes}
    return render(request, 'ledger/recipe_list.html', ctx)


def recipe(request, pk):
    ctx = {"recipe": Recipe.objects.get(pk=pk)}
    return render(request, 'ledger/recipe.html', ctx)


def image_create(request, pk):
    form = RecipeImageForm()
    
    if request.user.is_anonymous:
        return redirect('/accounts/login')
    
    if request.method == 'POST':
        form = RecipeImageForm(request.POST, request.FILES)

        if (form.is_valid()):
            t = RecipeImage()
            t.image = request.FILES.get('image')
            t.description = request.POST.get('description')
            t.recipe = Recipe.objects.get(pk=pk)
            t.save()
            
            return redirect(reverse('ledger:recipe', args=[pk]))
    
    ctx = {"recipe": Recipe.objects.get(pk=pk)}
    return render(request, 'ledger/image_add.html', ctx)
