from unittest import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import CreditCard
from .serializers import CreditCardSerializer
from .credit_card_manager import CreditCardManager


class ViewCreditCardTest(APITestCase):

    def test_invalid_card(self):
        """
        This test ensures that all songs added in the setUp method
        exist when we make a GET request to the songs/ endpoint
        """

        url = reverse('credit_card_view')
        data = {'full_credit_card_number':'0'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_card(self):
        """
        This test ensures that all songs added in the setUp method
        exist when we make a GET request to the songs/ endpoint
        """

        url = reverse('credit_card_view')
        data = {'full_credit_card_number':'4412345678997969'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)