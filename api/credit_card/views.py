from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CreditCard
from .serializers import CreditCardSerializer
from .credit_card_manager import CreditCardManager

@api_view(['GET','POST'])
def credit_card_view(request):
    if(request.method == 'GET'):
        serializer = CreditCardSerializer(CreditCard())
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CreditCardSerializer(data = request.data)
        if serializer.is_valid():

            credit_card_manager = CreditCardManager()
            credit_card = credit_card_manager.parse_credit_card(serializer.validated_data.get('full_credit_card_number'))
            if(credit_card_manager.validate_credit_card(credit_card)):
                serializer = CreditCardSerializer(credit_card)
            
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def generate_visa_view(request):
    if request.method == 'POST':
        visa = CreditCardManager().generate_visa()
        serializer = CreditCardSerializer(visa)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

@api_view(['POST'])
def generate_mastercard_view(request):
    if request.method == 'POST':
        mastercard = CreditCardManager().generate_mastercard()
        serializer = CreditCardSerializer(mastercard)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

@api_view(['POST'])
def generate_discover_view(request):
    if request.method == 'POST':
        discover = CreditCardManager().generate_discover()
        serializer = CreditCardSerializer(discover)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

@api_view(['POST'])
def generate_american_express_view(request):
    if request.method == 'POST':
        american_express = CreditCardManager().generate_american_express()
        serializer = CreditCardSerializer(american_express)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

