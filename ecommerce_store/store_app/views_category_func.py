from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CategoryModel
from .serializers import CategorySerializer

# Create your views here.

@api_view(['GET'])
def get_categories(request):
    products = CategoryModel.objects.all()
    serializer = CategorySerializer(products, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_category(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH'])
def category(request, pk):
    try:
        category = CategoryModel.objects.get(pk = pk)
    except CategoryModel.DoesNotExist:
        return Response({"error": "Product not found"},status=status.HTTP_404_NOT_FOUND)
        
    if not category:
        print(f'{pk} ID NOT FOUND')
        return  Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        return Response(CategorySerializer(category).data)
    
    serializer = CategorySerializer(
        category, 
        data=request.data,
        partial= request.method == 'PATCH'
    )
    if not serializer.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    serializer.save()
    return Response(serializer.data)