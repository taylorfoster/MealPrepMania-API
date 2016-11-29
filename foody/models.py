from django.db import models
from datetime import datetime


class Recipe(models.Model):
    title = models.CharField(max_length=100, blank=True, default='Meatballs')
    def __str__(self):
        return self.title
        
    #directions = models.ForeignKey(Direction, on_delete=models.CASCADE, null=True)
    #ingredients = models.ForeignKey(Ingredient, on_delete=models.CASCADE, null=True)
    
    class Meta:
        ordering = ('title',)#'created',)
    
class Direction(models.Model):
    recipe = models.ForeignKey(Recipe, related_name="directions", db_column='recipe')
    text = models.CharField(max_length=100, blank=True, default='Ball some meat')
    
        
class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, related_name="ingredients", db_column='recipe')
    name = models.CharField(max_length=100, blank=True, default='Meat')
    measurement = models.CharField(max_length=100, blank=True, default='cup')
    quantity = models.FloatField(default=1)
    
class GroceryItem(models.Model):
    isPurchased = models.BooleanField(default=False)
    name = models.CharField(max_length=100, blank=True, default='Meat')
    measurement = models.CharField(max_length=100, blank=True, default='cup')
    quantity = models.FloatField(default=1)

class MenuItem(models.Model):
    recipe = models.ForeignKey(Recipe, db_column='recipe')
    date = models.DateTimeField(default=datetime.now, blank=True)