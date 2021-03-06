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
        instance.isPurchased = validated_data.get('isPurchased', instance.isPurchased)
        instance.name = validated_data.get('name', instance.name)
        instance.measurement = validated_data.get('measurement', instance.measurement)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.save()
        return instance

class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = ('id', 'text',)
        
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
        recipe.save()
        return recipe

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        directions = validated_data.get('directions', 'nope')
        instance.directions.clear()
        instance.ingredients.clear()
        for i in range(len(directions)):
            serializer = DirectionSerializer(data=directions[i])
            if serializer.is_valid():
                serializer.save()
            direction = Direction.objects.create(**serializer.validated_data)
            instance.directions.add(direction)
        ingredients = validated_data.get('ingredients', 'nope')
        for i in range(len(ingredients)):
            serializer = IngredientSerializer(data=ingredients[i])
            if serializer.is_valid():
                serializer.save()
            ingredient = Ingredient.objects.create(**serializer.validated_data)
            instance.ingredients.add(ingredient)
        instance.save()
        return instance
       
class MenuItemSerializer(serializers.ModelSerializer):
    recipe = RecipeSerializer(many=True, required=False)
    class Meta:
        model = MenuItem
        fields = ('id', 'recipe', 'date')
        
    def create(self, validated_data):
        recipe_data = validated_data.pop('recipe')
        menuItem = MenuItem.objects.create(**validated_data)
        for i in range(len(recipe_data)):
            recipe = Recipe.objects.get(title=recipe_data[i]["title"])
            menuItem.recipe.add(recipe)
        menuItem.save()
        return menuItem
        
    def update(self, instance, validated_data):
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance

    