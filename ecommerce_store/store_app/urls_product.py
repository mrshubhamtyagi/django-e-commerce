from django.urls import path
from .views_product_function import get_products, add_product

urlpatterns = [
    path('', get_products, name='Products'),
    path('add/', add_product, name = 'Add Product')
]
