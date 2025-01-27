from rest_framework import generics
from .models import ProductModel
from .serializers import ProductSerializer
from rest_framework import status
from rest_framework.response import Response

class ProductList(generics.ListAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
        # return Response(serializer.data)