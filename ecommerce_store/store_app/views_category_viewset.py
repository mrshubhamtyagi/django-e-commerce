from functools import partial

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import CategoryModel
from .serializers import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

#----------THESE ARE OPTIONAL OVERRIDE METHODS----------
    
    # Override the create method (POST)
    def create(self, request, *args, **kwargs):
        data = request.data
        if len(data['name']) > 3:
            serializer = self.get_serializer(data = data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'error':'Custom Logic - name must be > 3 characters'})


    # Override the retrieve method (GET)
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        data['custom_logic'] = 'Custom Logic - added additional information'
        return Response(data)


    # Override the update method (PUT)
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        partial = kwargs.pop('partial', False)
        serializer = self.get_serializer(instance, data = request.data, partial = partial)
        
        if request.data.get('name'):
            request.data['name'] = request.data.get('name').upper()
        
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    # Override the partial_update method (PATCH)
    def partial_update(self, request, *args, **kwargs):        
        kwargs['partial'] = True
        # we can directly call the update function defined above
        #return self.update(request, *args, **kwargs)
        
        instance = self.get_object()
        serializer = self.get_serializer(instance, data = request.data, partial= True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    # Override the destroy method (DELETE)
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.pk is 1:
            return Response({'error':'Custom Logic - first item is not deletable'})
        else:
            self.perform_destroy(instance)
            return Response({'msg':'Deleted'}, status=status.HTTP_204_NO_CONTENT)
        
        