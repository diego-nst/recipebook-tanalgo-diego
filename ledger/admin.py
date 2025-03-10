from django.contrib import admin
from .models import Recipe, RecipeIngredient, Ingredient


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    search_fields = ('name',)
    inlines = [RecipeIngredientInline,]


class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)


# Register your models here.
