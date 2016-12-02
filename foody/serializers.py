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
        """
        print 'hi'
        print validated_data.get('name', instance.name)
        print 'hi again'
        """
        instance.save()
        return instance

class DirectionSerializer(serializers.ModelSerializer):
    #recipe = RecipeSerializer(many=True, read_only=True)
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
        #Direction.objects.create(recipe=recipe, **direction_data)
        #Ingredient.objects.create(recipe=recipe, **ingredient_data)
        return recipe #.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print 'validated data'
        print validated_data
        print 'end val'
        #instance.menuItem = validated_data.get('menuItem', instance.menuItem)
        print 'error here?'
        instance.title = validated_data.get('title', instance.title)
        directions = validated_data.get('directions', 'nope')
        instance.directions.clear()
        instance.ingredients.clear()
        #print directions
        for i in range(len(directions)):
            serializer = DirectionSerializer(data=directions[i])
            if serializer.is_valid():
                serializer.save()
            direction = Direction.objects.create(**serializer.validated_data)
            instance.directions.add(direction)
        ingredients = validated_data.get('ingredients', 'nope')
        print ingredients
        for i in range(len(ingredients)):
            print ingredients[i]
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
        print 'create'
        recipe_data = validated_data.pop('recipes')
        menuItem = MenuItem.objects.create(**validated_data)
        Recipe.objects.create(menuItem=menuItem, **recipe_data)
        return menuItem #.objects.create(**validated_data)
        
    def update(self, instance, validated_data):
        print 'meh'
        """stuff = validated_data.get('recipe')[0]
        print 'wtf'
        print stuff
        recipeID = getattr(stuff, 'id')
        """
        
        #print recipeID
        #print(validated_data.get('recipe'))
        #print(validated_data.get('recipe')[0]["id"])
        instance.recipe = instance.recipe
        #instance.recipe = Recipe.objects.get(pk=validated_data.get('recipe')[0])
        #instance.recipe = validated_data.get('recipe', instance.recipe) #was commented
        instance.date = validated_data.get('date', instance.date)
        """
        recipes = validated_data.get('recipe', 'nope')
        instance.recipe.clear()
        for i in range(len(recipes)):
            print recipes[i]
            serializer = RecipeSerializer(data=recipes[i])
            if serializer.is_valid():
                serializer.save()
            recipe = Recipe.objects.create(**serializer.validated_data)
            instance.recipe.add(recipe)
        """
        instance.save()
        return instance

    