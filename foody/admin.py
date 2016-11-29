from django.contrib import admin

from .models import Recipe, Ingredient, Direction

class IngredientsInline(admin.StackedInline):
    model = Ingredient
    extra = 1
    
class DirectionsInline(admin.StackedInline):
    model = Direction
    extra = 1

class RecipeAdmin(admin.ModelAdmin):
    fields = ['title']
    inlines = [IngredientsInline, DirectionsInline]

admin.site.register(Recipe, RecipeAdmin)