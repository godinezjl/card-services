#from django.db import models

class CreditCard():
    def __init__ (self, 
            full_credit_card_number = '',
            major_industry_identifier = 0,
            issuer_identification_number = 0,
            personal_account_number = 0,
            check_digit = 0,
            issuer = 'Unkown',
            ):
        self.full_credit_card_number = full_credit_card_number
        self.major_industry_identifier = major_industry_identifier
        self.issuer_identification_number = issuer_identification_number
        self.personal_account_number = personal_account_number
        self.check_digit = check_digit
        self.issuer = issuer

class InvalidCreditCard(CreditCard):
    def __init__ (self,full_credit_card_number):
        super().__init__(full_credit_card_number)
