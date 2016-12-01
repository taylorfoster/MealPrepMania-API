from rest_framework import serializers
from foody.models import Recipe, Direction, Ingredient, GroceryItem, MenuItem

        
class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'measurement', 'quantity',)
        
    
    def create(self, validated_data):
        return Ingredient.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.recipe = validated_data.get('recipe', instance.recipe)
        instance.name = validated_data.get('name', instance.name)
        instance.measurement = validated_data.get('measurement', instance.measurement)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.save()
        return instance
        
class GroceryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroceryItem
        fields = ('id', 'isPurchased', 'name', 'measurement', 'quantity')
        
    
    def create(self, validated_data):
        return GroceryItem.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print 'updating'
        print(validated_data)
        instance.isPurchased = validated_data.get('isPurchased', instance.isPurchased)
        instance.name = validated_data.get('name', instance.name)
        instance.measurement = validated_data.get('measurement', instance.measurement)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        print 'hi'
        print validated_data.get('name', instance.name)
        print 'hi again'
        instance.save()
        return instance

class DirectionSerializer(serializers.ModelSerializer):
    #recipe = RecipeSerializer(many=True, read_only=True)
    class Meta:
        model = Direction
        fields = ('id', 'text',) #fields = ('recipe', 'text',)
        
    def create(self, validated_data):
        return Direction.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.recipe = validated_data.get('recipe', instance.recipe)
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance
        
class RecipeSerializer(serializers.ModelSerializer):
    
    directions = DirectionSerializer( many=True)
    ingredients = IngredientSerializer( many=True)
    class Meta:
        model = Recipe
        fields = ('id', 'title', 'directions', 'ingredients')
    
    def create(self, validated_data):
        direction_data = validated_data.pop('directions')
        ingredient_data = validated_data.pop('ingredients')
        recipe = Recipe.objects.create(**validated_data)
        Direction.objects.create(recipe=recipe, **direction_data)
        Ingredient.objects.create(recipe=recipe, **ingredient_data)
        return Recipe.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.menuItem = validated_data.get('menuItem', instance.menuItem)
        instance.title = validated_data.get('title', instance.title)
        instance.directions = validated_data.get('directions', instance.directions)  #commented these two
        instance.ingredients = validated_data.get('ingredients', instance.ingredients)
        instance.save()
        return instance
        
class MenuItemSerializer(serializers.ModelSerializer):
    def clean_recipe(self, data):
        print(data)
        data['recipe'] = Recipe.objects.get(pk=data['recipe'])
        print(data)
        return data
   
    recipe = RecipeSerializer(many=True, required=False, validators=[clean_recipe])
    class Meta:
        model = MenuItem
        fields = ('id', 'recipe', 'date')
        
    def create(self, validated_data):
        recipe_data = validated_data.pop('recipes')
        menuItem = MenuItem.objects.create(**validated_data)
        Recipe.objects.create(menuItem=menuItem, **recipe_data)
        return menuItem.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print(validated_data.get('recipe'))
        print(validated_data.get('recipe')[0])
        instance.recipe = Recipe.objects.get(pk=validated_data.get('recipe')[0])
        #instance.recipe = validated_data.get('recipe', instance.recipe) #was commented
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance