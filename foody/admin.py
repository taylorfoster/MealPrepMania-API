from django.contrib import admin

from .models import Recipe, Ingredient, Direction, GroceryItem, MenuItem

class IngredientsInline(admin.StackedInline):
    model = Ingredient
    extra = 1
    
class DirectionsInline(admin.StackedInline):
    model = Direction
    extra = 1
    
class RecipesInline(admin.StackedInline):
    model = Recipe
    extra = 0

class RecipeAdmin(admin.ModelAdmin):
    fields = ['title']
    inlines = [IngredientsInline, DirectionsInline]
    
class GroceryItemAdmin(admin.ModelAdmin):
    fields = ['name', 'measurement', 'quantity', 'isPurchased']
    
class MenuItemAdmin(admin.ModelAdmin):
    fields = ['date']
    inlines = [RecipesInline]

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(GroceryItem, GroceryItemAdmin)
admin.site.register(MenuItem, MenuItemAdmin)