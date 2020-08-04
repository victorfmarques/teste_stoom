from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from ..models import Address
from .serializers import AddressSerializer

class AddressViewSet(viewsets.ModelViewSet):

    queryset            = Address.objects.all()
    serializer_class    = AddressSerializer
    filter_backends     = (DjangoFilterBackend,)
    filter_fields       = '__all__'

