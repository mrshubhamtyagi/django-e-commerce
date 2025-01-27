from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import CategoryModel
from .serializers import CategorySerializer

class CategoryList(APIView):
    def get(self, request):
        categories = CategoryModel.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return JsonResponse({'data':serializer.data}, safe=False)


    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data)



class CategoryDetail(APIView):
    def get(self, request, pk):
        try:
            category = CategoryModel.objects.get(pk = pk)
            serializer= CategorySerializer(category)
            return Response(serializer.data)

        except CategoryModel.DoesNotExist:
            return Response({"error":"Category does not exist!"}, status= status.HTTP_404_NOT_FOUND)
        
    def put(self, request, pk):
        try:
            category = CategoryModel.objects.get(pk = pk)
            serializer = CategorySerializer(category, data=request.data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
            serializer.save()
            return Response(serializer.data)
            
        except CategoryModel.DoesNotExist:
            return Response({'error':'Does Not Exist'}, status = status.HTTP_404_NOT_FOUND)
        
       
        
        
    def patch(self, request, pk):
        try:
            category = CategoryModel.objects.get(pk = pk)
            serializer = CategorySerializer(category, data=request.data, partial=True)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
            serializer.save()
            return Response(serializer.data)
        
        except CategoryModel.DoesNotExist:
            return Response({'error': 'Does Not Exist'}, status = status.HTTP_404_NOT_FOUND)
        
       
    
    
    def delete(self, request, pk):
        try:
            category = CategoryModel.objects.get(pk = pk)
            category.delete()
            return Response({'msg':'Deleted successfully'}, status = status.HTTP_200_OK)
        
        except CategoryModel.DoesNotExist:
            return Response({'error': 'Does Not Exist'}, status = status.HTTP_404_NOT_FOUND)

        
        
        
                
        
            
        