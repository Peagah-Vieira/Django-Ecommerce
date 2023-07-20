from rest_framework.viewsets import ModelViewSet
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer


class OrdersAPIViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemsViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
