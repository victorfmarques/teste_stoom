from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from addresses.api.viewsets import AddressViewSet

# Definição de Rotas da API
router = routers.DefaultRouter()
router.register(r'addresses', AddressViewSet)

# Definição das URLs do projeto
urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
