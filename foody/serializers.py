from rest_framework import serializers
from foody.models import Recipe, Direction, Ingredient, GroceryItem, MenuItem#, LANGUAGE_CHOICES, STYLE_CHOICES

        
class IngredientSerializer(serializers.ModelSerializer):
    #recipe = RecipeSerializer(many=True, read_only=True)
    class Meta:
        model = Ingredient
        fields = ('name', 'measurement', 'quantity',) #fields = ('recipe', 'name', 'measurement', 'quantity',)
        
    
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
        fields = ('isPurchased', 'name', 'measurement', 'quantity')
        
    
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
    #recipe = RecipeSerializer(many=True, read_only=True)
    class Meta:
        model = Direction
        fields = ('text',) #fields = ('recipe', 'text',)
        
    def create(self, validated_data):
        return Direction.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.recipe = validated_data.get('recipe', instance.recipe)
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance
        
class RecipeSerializer(serializers.ModelSerializer):
    
    directions = DirectionSerializer(source='*', many=True, read_only=True)
    ingredients = IngredientSerializer(source='*', many=True, read_only=True)
    class Meta:
        model = Recipe
        fields = ('id', 'title', 'directions', 'ingredients')
        depth = 1
    
    def create(self, validated_data):
        return Recipe.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        #instance.directions = validated_data.get('directions', instance.directions)
        #instance.ingredients = validated_data.get('ingredients', instance.ingredients)
        instance.save()
        return instance
        
class MenuItemSerializer(serializers.ModelSerializer):
    #recipe = RecipeSerializer(many=True, read_only=True)
    class Meta:
        model = MenuItem
        fields = ('recipe', 'date')
        
    def create(self, validated_data):
        return Direction.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.recipe = validated_data.get('recipe', instance.recipe)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance