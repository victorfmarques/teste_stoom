import json
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from addresses.api.serializers import AddressSerializer
from addresses.models import Address

class ListAddressTestCase(APITestCase):

    list_url = '/api/addresses/'

    def test_address_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateAddressTestCase(APITestCase):

    list_url = '/api/addresses/'

    def setUp(self):

        self.data = {
                "street_name": "teste",
                "number": 83,
                "complement": "",
                "neighbourhood": "teste teste",
                "city": "teste",
                "state": "teste teste",
                "country": "teste",
                "zipcode": 13467666,
                "latitude": 0,
                "longitude": 0 
            }

    def test_address_create(self):
        response = self.client.post(self.list_url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED) 
         

class UpdateAddressTestCase(APITestCase):

    list_url = '/api/addresses/'

    def setUp(self):
        self.address = Address.objects.create(
            street_name="teste",
            number=83,
            complement="",
            neighbourhood= "teste teste",
            city="teste",
            state="teste teste",
            country= "teste",
            zipcode= 13467666,
            latitude= 10,
            longitude= 10
        )
        self.address.save()

        self.data = {
            "street_name": "teste",
            "number": 83,
            "complement": "",
            "neighbourhood": "bairro",
            "city": "cidade",
            "state": "estado",
            "country": "pais",
            "zipcode": 13467666,
            "latitude": 10,
            "longitude": 10 
        }
        
    def test_address_update(self):
        response = self.client.put(self.list_url+ f'{self.address.pk}/', data=self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK) 

class DeleteAddressTestCase(APITestCase):

    list_url = '/api/addresses/'

    def setUp(self):
        self.address = Address.objects.create(
            street_name="teste",
            number=83,
            complement="",
            neighbourhood= "teste teste",
            city="teste",
            state="teste teste",
            country= "teste",
            zipcode= 13467666,
            latitude= 10,
            longitude= 10
        )
        self.address.save()


    def test_address_delete(self):
        response = self.client.delete(self.list_url+ f'{self.address.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT) 