from rest_framework import serializers
from foody.models import Recipe, Direction, Ingredient, LANGUAGE_CHOICES, STYLE_CHOICES

        
class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('name', 'measurement', 'quantity',)
        
    
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Ingredient.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.measurement = validated_data.get('measurement', instance.measurement)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.save()
        return instance
        
class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = ('text',)
        
    
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Direction.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance
        
class FoodySerializer(serializers.ModelSerializer):
    direction = DirectionSerializer(many=True, read_only=True)
    ingredient = IngredientSerializer(many=True, read_only=True)
    class Meta:
        model = Recipe
        depth = 2
        fields = ('id', 'title', 'direction', 'ingredient')
        
    
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
        instance.direction = validated_data.get('direction', instance.direction)
        instance.ingredient = validated_data.get('ingredient', instance.ingredient)
        instance.save()
        return instance