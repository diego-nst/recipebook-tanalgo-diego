from django.contrib import admin
from .models import Recipe, RecipeIngredient, Ingredient, RecipeImage


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class RecipeImageInline(admin.TabularInline):
    model = RecipeImage


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    search_fields = ('name',)
    inlines = [RecipeIngredientInline, RecipeImageInline]


class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)


# Register your models here.
