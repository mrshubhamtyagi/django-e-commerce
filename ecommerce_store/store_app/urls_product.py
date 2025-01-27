from django.urls import path
from .views_product_function import get_products, add_product
from .views_product_class import ProductList

urlpatterns = [
    path('', ProductList.as_view(), name='Products List'),
    # path('add/', add_product, name = 'Add Product')
]
