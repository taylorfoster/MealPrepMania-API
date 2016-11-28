from django.db import models
#from pygments.lexers import get_all_lexers
#from pygments.styles import get_all_styles

#LEXERS = [item for item in get_all_lexers() if item[1]]
#LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
#STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class Recipe(models.Model):
    #created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='Meatballs')
    #directions = models.ForeignKey(Direction, on_delete=models.CASCADE, null=True)
    #ingredients = models.ForeignKey(Ingredient, on_delete=models.CASCADE, null=True)
    
    class Meta:
        ordering = ('title',)#'created',)
    
class Direction(models.Model):
    recipe = models.ForeignKey(Recipe, db_column='recipe')
    text = models.CharField(max_length=100, blank=True, default='Ball some meat')
    
class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, db_column='recipe')
    name = models.CharField(max_length=100, blank=True, default='Meat')
    measurement = models.CharField(max_length=100, blank=True, default='cup')
    quantity = models.CharField(max_length=100, blank=True, default='1')
    
class GroceryList(models.Model):
    isPurchased = models.BooleanField(default=False)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

