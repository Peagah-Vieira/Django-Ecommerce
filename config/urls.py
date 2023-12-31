from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

# Django-Ecommerce URLs
urlpatterns = [
    path(
        'accounts/',
        include('accounts.urls'),
    ),
    path(
        'products/',
        include('products.urls'),
    ),
    path(
        'orders/',
        include('orders.urls'),
    ),
]

# Django Application URLs
urlpatterns += [
    path('admin/', admin.site.urls),
]

# JWT Authentication URLs
urlpatterns += [
    path(
        'api/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'api/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
    path(
        'api/token/verify/',
        TokenVerifyView.as_view(),
        name='token_verify'
    ),
]
