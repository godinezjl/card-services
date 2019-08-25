from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CreditCard
from .credit_card_serializer import CreditCardSerializer
from .credit_card_manager import CreditCardManager

@api_view(['GET','POST'])
def credit_card_view(request):
    '''
    display the credit card or validate the credit card info
    '''
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
