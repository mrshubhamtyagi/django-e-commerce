from django.urls import path
# from .views_category_func import get_categories, category
from .views_category_class import CategoryList, CategoryDetail
urlpatterns = [
    path('', CategoryList.as_view(), name='Categories List'),
    path('<int:pk>/', CategoryDetail.as_view(), name='Category Details'),
]
