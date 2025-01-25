from django.shortcuts import render
from rest_framework.decorators import api_view
from  rest_framework.response import Response
from rest_framework import status
from .models import ProductModel
from .serializers import ProductSerializer

# Create your views here.

@api_view(['GET'])
def get_products(request):
    products = ProductModel.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'PATCH'])
def update_product(request, pk):
    product=ProductModel.objects.get(pk=pk)
    if not product:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer=ProductSerializer(product, data=request.data, partial=request.method =='PATCH')
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    serializer.save()
    return Response(serializer.data)
    
        