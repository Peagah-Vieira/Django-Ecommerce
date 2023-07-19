from rest_framework.routers import SimpleRouter
from products import views

app_name = "products"

products_api_router = SimpleRouter(trailing_slash=True)
products_api_router.register(
    prefix='api',
    viewset=views.ProductsAPIViewSet,
    basename='products-api'
)

urlpatterns = products_api_router.urls
