from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from foody.models import Recipe
from foody.serializers import FoodySerializer
from foody.models import Direction
from foody.serializers import DirectionSerializer
from foody.models import Ingredient
from foody.serializers import IngredientSerializer
from foody.models import GroceryList
from foody.serializers import GroceryListSerializer
from django.http import JsonResponse

@api_view(['GET', 'POST'])
def snippet_list(request, format=None):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Recipe.objects.all()
        serializer = FoodySerializer(snippets, many=True)
        return Response(serializer.data)
        #return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = FoodySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk, format=None):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        snippet = Recipe.objects.get(pk=pk)
    except Recipe.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FoodySerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FoodySerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)