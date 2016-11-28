from django.contrib import admin

from .models import Recipe, Ingredient, Direction

class IngredientsInline(admin.StackedInline):
    model = Ingredient
    extra = 3

class RecipeAdmin(admin.ModelAdmin):
    fields = ['title']
    inlines = [IngredientsInline]

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Direction)