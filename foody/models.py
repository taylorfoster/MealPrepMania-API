from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Recipe(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='Meatballs')
    direction = models.CharField(max_length=100, blank=True, default='Stir')
    ingredient = models.CharField(max_length=100, blank=True, default='Balls')
    
class Direction(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='+', blank=True, null=True)
    text = models.CharField(max_length=100, blank=True, default='Ball some meat')
    
class Ingredient(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    recipe = models.ForeignKey(Recipe, related_name='+', blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, default='Meat')
    measurement = models.CharField(max_length=100, blank=True, default='3/4 cup')
    quantity = models.CharField(max_length=100, blank=True, default='1')

    class Meta:
        ordering = ('created',)