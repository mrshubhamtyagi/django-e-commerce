from django.urls import path
from rest_framework.routers import DefaultRouter
from .views_category_func import get_categories, category
from .views_category_class import CategoryList, CategoryDetail
from .views_category_viewset import CategoryViewSet

# used in Function and Class based Views
urlpatterns = [
    path('', CategoryList.as_view(), name='Categories List'),
    path('<int:pk>/', CategoryDetail.as_view(), name='Category Details'),
]

# use this in case of Viewset Approach
# router = DefaultRouter()
# router.register(r"categories", CategoryViewSet, basename='Category')
# urlpatterns = router.urls
