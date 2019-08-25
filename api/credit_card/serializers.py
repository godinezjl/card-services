from rest_framework import serializers
from .models import CreditCard

# class CreditCardSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CreditCard
#         fields = [
#                 'full_credit_card_number',
#                 'major_industry_identifier',
#                 'issuer_identification_number',
#                 'personal_account_number',
#                 'check_digit',
#                 'issuer'
#                 ]

class CreditCardSerializer(serializers.Serializer):
    full_credit_card_number = serializers.CharField(allow_blank=True, max_length=19)
    major_industry_identifier = serializers.IntegerField(read_only = True)
    issuer_identification_number = serializers.IntegerField(read_only = True)
    personal_account_number = serializers.IntegerField(read_only = True)
    check_digit = serializers.IntegerField(read_only = True)
    issuer = serializers.CharField(required=False, allow_blank=True, max_length=50)

    def create(self, validated_data):
        '''
        Create and return a new CreditCard instance based on the validated data
        '''
        return CreditCard(
            validated_data.get('full_credit_card_number'),
            validated_data.get('major_industry_identifier'),
            validated_data.get('issuer_identification_number'),
            validated_data.get('personal_account_number'),
            validated_data.get('check_digit'),
            validated_data.get('issuer')
        )

    def update(self, instance, validated_data):
        '''
        Update and return an updated credit card instance given the validated data
        '''
        instance.full_credit_card_number = validated_data.get('full_credit_card_number', instance.full_credit_card_number),
        instance.major_industry_identifier = validated_data.get('major_industry_identifier', instance.major_industry_identifier),
        instance.issuer_identification_number = validated_data.get('issuer_identification_number', instance.issuer_identification_number),
        instance.personal_account_number = validated_data.get('personal_account_number', instance.personal_account_number),
        instance.check_digit = validated_data.get('check_digit', instance.check_digit),
        instance.issuer = validated_data.get('issuer', instance.issuer)
        instance.save()
        return instance


