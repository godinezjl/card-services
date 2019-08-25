# from django.test import TestCase
# from django.urls import reverse
# from rest_framework.test import APITestCase, APIClient
# from rest_framework.views import status
# from .models import CreditCard
# from .serializers import CreditCardSerializer

# Create your tests here.

# class BaseViewTest(APITestCase):
#     client = APIClient()

#     credit_card = CreditCard('1234567')
    # @staticmethod
    # def create_(title="", artist=""):
    #     if title != "" and artist != "":
    #         Songs.objects.create(title=title, artist=artist)

    # def setUp(self):
    #     # add test data
    #     self.create_song("like glue", "sean paul")
    #     self.create_song("simple song", "konshens")
    #     self.create_song("love is wicked", "brick and lace")
    #     self.create_song("jam rock", "damien marley")


# class ValidateCreditCardTest(BaseViewTest):

#     def test_validate_credit_card(self):
#         """
#         This test ensures that all songs added in the setUp method
#         exist when we make a GET request to the songs/ endpoint
#         """
#         # hit the API endpoint
#         response = self.client.get(
#             reverse("validate-creditcard", kwargs={"version": "v1"})
#         )
#         # fetch the data from db
#         serialized = CreditCardSerializer(credit_card, many=False)
#         self.assertEqual(response.data, serialized.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)