from rest_framework.routers import SimpleRouter
from orders import views

app_name = "orders"

orders_api_router = SimpleRouter(trailing_slash=True)
orders_api_router.register(
    prefix='api',
    viewset=views.OrdersAPIViewSet,
    basename='orders-api'
)

urlpatterns = orders_api_router.urls
