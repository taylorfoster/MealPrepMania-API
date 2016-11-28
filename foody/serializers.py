from rest_framework import serializers
from foody.models import Recipe, Direction, Ingredient, GroceryList#, LANGUAGE_CHOICES, STYLE_CHOICES

class FoodySerializer(serializers.ModelSerializer):
    #directions = DirectionSerializer(many=True, read_only=True)
    #ingredients = IngredientSerializer(many=True, read_only=True)
    class Meta:
        model = Recipe
        #depth = 2
        fields = ('id', 'title',) # 'directions', 'ingredients')
        
    
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Recipe.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        #instance.directions = validated_data.get('directions', instance.directions)
        #instance.ingredients = validated_data.get('ingredients', instance.ingredients)
        instance.save()
        return instance
        
class IngredientSerializer(serializers.ModelSerializer):
    recipe = FoodySerializer(many=True, read_only=True)
    class Meta:
        model = Ingredient
        fields = ('recipe', 'name', 'measurement', 'quantity',)
        
    
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Ingredient.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('recipe', instance.recipe)
        instance.name = validated_data.get('name', instance.name)
        instance.measurement = validated_data.get('measurement', instance.measurement)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.save()
        return instance
        
class GroceryListSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer(many=False, read_only=True)
    class Meta:
        model = GroceryList
        fields = ('isPurchased', 'ingredient',)
        
    
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return GroceryList.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.isPurchased = validated_data.get('isPurchased', instance.isPurchased)
        instance.ingredient = validated_data.get('ingredient', instance.ingredient)
        instance.save()
        return instance
        
class DirectionSerializer(serializers.ModelSerializer):
    recipe = FoodySerializer(many=True, read_only=True)
    class Meta:
        model = Direction
        fields = ('recipe', 'text',)
        
    
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Direction.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('recipe', instance.recipe)
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance
        
