from rest_framework import serializers
from rest_framework.utils.representation import manager_repr
from .models import ProductModel, CategoryModel

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['id', 'name', 'description']

    # Custom validation to ensure description is greater than 3 characters 
    # validate_<field_name> focuses on the suffix key only
    def validate_description(self, value):
        if len(value) < 4:
            raise serializers.ValidationError("Description must be greater than 3 characters")
        return value

    # Custom validation to ensure Name is greater than 3 characters
    # this receives the whole data
    def validate(self, data):
        if 'name' in data and len(data['name']) < 4:
            raise serializers.ValidationError("Name must be greater than 3 characters")
        return data



class ProductSerializer(serializers.ModelSerializer):
    # using the CategorySerializer from above to nest the category data 
    category = CategorySerializer(read_only = True)
    
    # showing only required data from Category at ROOT level in JSON
    # category_name = serializers.CharField(source='category.name')
    # category_description = serializers.CharField(source='category.description') 
    
    #use this to return extra fields by calling a method defined in this class only
    total_price = serializers.SerializerMethodField()
    
    #use get_<fieldname> to link method to the field
    def get_total_price(self, obj):
        return obj.price * obj.stock

    class Meta:
        model = ProductModel
        fields = [
            'id', 
            'name', 
            'description', 
            'price', 
            'stock', 
            'category',
            # 'category_name', 
            # 'category_description',
            'total_price',
            'is_available', #using model property as extra field
            
        ]