from django.contrib import admin

from .models import Recipe, Ingredient, Direction, GroceryItem

class IngredientsInline(admin.StackedInline):
    model = Ingredient
    extra = 1
    
class DirectionsInline(admin.StackedInline):
    model = Direction
    extra = 1

class RecipeAdmin(admin.ModelAdmin):
    fields = ['title']
    inlines = [IngredientsInline, DirectionsInline]
    
#class GroceryListAdmin(admin.ModelAdmin):
   # fields = ['name', 'measurement', 'quantity', 'isPurchased']

admin.site.register(Recipe, RecipeAdmin)