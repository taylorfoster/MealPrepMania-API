from django.db import models
from datetime import datetime

class MenuItem(models.Model):
    date = models.DateTimeField(default=datetime.now, blank=True, null=True)
    def __str__(self):
        return str(self.date)
    class Meta:
        ordering = ('date',)

class Recipe(models.Model):
    menuItem = models.ForeignKey(MenuItem, related_name="recipe", db_column='menuItem', null=True, blank=True)
    title = models.CharField(max_length=100, blank=True, default='Recipe Title')
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('title',)
    
class Direction(models.Model):
    recipe = models.ForeignKey(Recipe, related_name="directions", db_column='recipe', null=True, blank=True)
    text = models.CharField(max_length=100, blank=True, default='Ball some meat')
    
        
class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, related_name="ingredients", db_column='recipe', null=True, blank=True)
    name = models.CharField(max_length=100, blank=True, default='Meat')
    measurement = models.CharField(max_length=100, blank=True, default='cup')
    quantity = models.FloatField(default=1.0)
    
class GroceryItem(models.Model):
    isPurchased = models.BooleanField(default=False)
    name = models.CharField(max_length=100, blank=True, default='Meat')
    measurement = models.CharField(max_length=100, blank=True, default='cup')
    quantity = models.FloatField(default=1.0)
    
    def __str__(self):
        return self.name

