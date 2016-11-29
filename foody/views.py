from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from foody.models import Recipe
from foody.serializers import FoodySerializer
from foody.models import Direction
from foody.serializers import DirectionSerializer
from foody.models import Ingredient
from foody.serializers import IngredientSerializer
from foody.models import GroceryItem
from foody.serializers import GroceryListSerializer
from foody.models import MenuItem
from foody.serializers import MenuItemSerializer
from django.http import JsonResponse

@api_view(['GET', 'POST'])
def recipe_list(request, format=None):
    if request.method == 'GET':
        recipes = Recipe.objects.all().values()
        serializer = FoodySerializer(recipes, many=True)
        return Response(serializer.data)
        #return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = FoodySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'POST'])        
def groceryList_list(request, format=None):
    if request.method == 'GET':
        groceryList = GroceryItem.objects.all()
        serializer = GroceryListSerializer(groceryList, many=True)
        return Response(serializer.data)
        #return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = GroceryListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'POST'])
def menu_list(request, format=None):
    if request.method == 'GET':
        menu = MenuItem.objects.all().values()
        serializer = MenuItemSerializer(menu, many=True)
        return Response(serializer.data)
        #return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = MenuItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
@api_view(['GET', 'PUT', 'DELETE'])
def recipe_detail(request, pk, format=None):
    try:
        recipe = Recipe.objects.get(pk=pk)
    except Recipe.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FoodySerializer(recipe)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FoodySerializer(recipe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
  
@api_view(['GET', 'PUT', 'DELETE'])      
def groceryList_detail(request, pk, format=None):
    try:
        groceryList = GroceryItem.objects.get(pk=pk)
    except GroceryItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GroceryListSerializer(groceryList)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GroceryListSerializer(groceryList, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        groceryList.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
@api_view(['GET', 'PUT', 'DELETE'])
def menu_detail(request, pk, format=None):
    try:
        menu = MenuItem.objects.get(pk=pk)
    except MenuItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MenuItemSerializer(menu)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MenuItemSerializer(menu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        menu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)