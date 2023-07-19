from rest_framework.viewsets import ModelViewSet
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class CategoriesAPIViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductsAPIViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
