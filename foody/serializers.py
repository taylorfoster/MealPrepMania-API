from rest_framework import serializers
from foody.models import Recipe, LANGUAGE_CHOICES, STYLE_CHOICES


class FoodySerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id', 'title', 'instructions')
    
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
        instance.instructions = validated_data.get('instructions', instance.instructions)
        instance.save()
        return instance