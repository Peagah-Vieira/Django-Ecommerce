from rest_framework.routers import SimpleRouter
from accounts import views

app_name = "accounts"

accounts_api_router = SimpleRouter(trailing_slash=True)
accounts_api_router.register(
    prefix='api',
    viewset=views.AccountsAPIViewSet,
    basename='accounts-api'
)

urlpatterns = accounts_api_router.urls
