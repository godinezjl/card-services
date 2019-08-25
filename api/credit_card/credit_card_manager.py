from .models import CreditCard, InvalidCreditCard
import re

class CreditCardManager: 
    '''
    Implements basic credit card operations

    Credit card logic taken from wikipedia 
    (not the most reliable source, but good enough for this excersice)

    List of supported credit cards:
    Card issuer           IIN                 Len
    ----------------------------------------------
    American Express	34, 37	            15

    Discover            6011,               16-19                            
                        622126 - 622925,
                        624000 - 626999,
                        628200 - 628899, 
                        64, 
                        65

    Mastercard          2221-2720,          16
                        51–55

    Visa                4,                  16
                        4571
    '''
    
    _american_express_mii = 3
    _discover_mii = 6
    _mastercard_original_mii = 2
    _mastercard_extended_mii = 5
    _visa_mii = 4
    message = ''

    def __init__ (self):
        pass
        
    def parse_credit_card(self, credit_card_number):
        major_industry_identifier = 0
        account_identification_number = 0
        issuer_identification_number = 0
        personal_account_number = 0
        check_digit = 0
        issuer = 'Unknown'

        # ensure credit card number is valid
        credit_card_number = self.__sanitize_credit_card_number(credit_card_number)

        # parse major industry identifier
        if len(credit_card_number) > 1:
            major_industry_identifier = int(credit_card_number[:1])
        else:
            return InvalidCreditCard(credit_card_number)

        if not self.__is_valid_credit_card_length(credit_card_number,major_industry_identifier):
            return InvalidCreditCard(credit_card_number)

        # parse account indentification number
        account_identification_number = credit_card_number[:-1]

        # parse the issuer identification number
        if major_industry_identifier == self._american_express_mii:
            issuer = 'American Express'
            issuer_identification_number = self.__get_american_express_identification_number(account_identification_number)

        elif major_industry_identifier == self._discover_mii:
            issuer = 'Discover'
            issuer_identification_number = self.__get_discover_identification_number(account_identification_number)

        elif major_industry_identifier == self._mastercard_original_mii or major_industry_identifier == self._mastercard_extended_mii:
            issuer = 'Master Card'
            issuer_identification_number = self.__get_mastercard_identification_number(account_identification_number)

        elif major_industry_identifier == self._visa_mii:
            issuer = 'Visa'
            issuer_identification_number = self.__get_visa_identification_number(account_identification_number)

        if issuer_identification_number == 0:
           return InvalidCreditCard(credit_card_number)

        # parse the personal account number
        personal_account_number = int(account_identification_number[len(str(issuer_identification_number)):])
        
        # parse the check digit
        check_digit = int(credit_card_number[-1:])

        return CreditCard(
            credit_card_number,
            major_industry_identifier,
            issuer_identification_number,
            personal_account_number,
            check_digit,
            issuer
            )

    def validate_credit_card(self, credit_card):
        return all (
            [
                credit_card.major_industry_identifier != 0,
                credit_card.personal_account_number != 0,
                credit_card.issuer_identification_number != 0,
                self.__validate_luhn_checksum(credit_card.full_credit_card_number)
            ]
        )
    
    def __sanitize_credit_card_number(self, credit_card_number):
        credit_card_number = re.sub(r"\s+", "", credit_card_number)
        credit_card_number = re.sub(r"-+", "", credit_card_number)
        return credit_card_number

    def __is_valid_credit_card_length(self, credit_card_number, major_industry_identifier):
        if all(
                [
                    major_industry_identifier == self._american_express_mii, 
                    len(credit_card_number) == 15
                ]
            ): return True

        if all(
                [
                    major_industry_identifier == self._discover_mii, 
                    len(credit_card_number) >= 16,
                    len(credit_card_number) <= 19
                ]
            ): return True

        if all(
                [
                    major_industry_identifier == self._mastercard_extended_mii, 
                    len(credit_card_number) == 16
                ]
            ): return True

        if all(
                [
                    major_industry_identifier == self._mastercard_original_mii, 
                    len(credit_card_number) == 16
                ]
            ): return True
        
        if all(
                [
                    major_industry_identifier == self._visa_mii, 
                    len(credit_card_number) == 16
                ]
            ): return True

        self.message = 'Invalid credit card number: not enough digits to process request.'
        return False

    def __get_american_express_identification_number(self, account_identification_number):
        if len(account_identification_number) > 2:
            parsed_account_number = int(account_identification_number[:2])

            # only return valid american express account numbers
            if parsed_account_number == 34 or parsed_account_number == 37:
                return parsed_account_number

        return 0

    def __get_discover_identification_number(self, account_identification_number):
        if len(account_identification_number) > 2:
            parsed_account_number = int(account_identification_number[:2])

            # only return valid discover account numbers 64 and 65
            if parsed_account_number == 64 or parsed_account_number == 65:
                return parsed_account_number

        if len(account_identification_number) > 4:
            parsed_account_number = int(account_identification_number[:4])

            # only return valid discover account number 6011
            if parsed_account_number == 6011:
                return parsed_account_number

        if len(account_identification_number) > 6:
            parsed_account_number = int(account_identification_number[:6])

            # only return valid discover account numbers between the ranges of
            # 622126 - 622925, 624000 - 626999, and 628200 - 628899
            if any([parsed_account_number >= 622126 and parsed_account_number <= 622925,
                    parsed_account_number >= 624000 and parsed_account_number <= 626999,
                    parsed_account_number >= 628200 and parsed_account_number <= 628899]):
                return parsed_account_number
            
        return 0

    def __get_mastercard_identification_number(self, account_identification_number):
        if len(account_identification_number) > 2:
            parsed_account_number = int(account_identification_number[:2])

            # only return valid mastercard account numbers between 51 and 55
            if parsed_account_number >= 51 and parsed_account_number <= 55:
                return parsed_account_number

        if len(account_identification_number) > 4:
            parsed_account_number = int(account_identification_number[:4])

            # only return valid discover account number between 2221-2720
            if parsed_account_number >= 2221 and parsed_account_number <= 2720:
                return parsed_account_number
        
        return 0

    def __get_visa_identification_number(self, account_identification_number):
        if len(account_identification_number) > 4:
            parsed_account_number = int(account_identification_number[:4])

            # only return valid visa account number 4571
            if parsed_account_number == 4571:
                return parsed_account_number
        
        if len(account_identification_number) > 1:
            parsed_account_number = int(account_identification_number[:1])

            # only return valid visa account number 4
            if parsed_account_number == 4:
                return parsed_account_number

        return 0

    def __validate_luhn_checksum(self, full_credit_card_number):

        # ensure string is properly formated
        full_credit_card_number = self.__sanitize_credit_card_number(full_credit_card_number)

        if not full_credit_card_number.isdigit():
            return False

        number_to_process = int(full_credit_card_number)
        sum=0

        while number_to_process:
            # get the right most two digits from the credit card number
            next_two_digits = number_to_process % 100

            # keep track of the first digit
            first_digit = next_two_digits % 10

            # multiply the second digit by 2
            second_digit_multiplied_by_two = next_two_digits // 10 * 2

            # add the first digit and the sum of the multiplication of the second digit
            sum += second_digit_multiplied_by_two // 10 + second_digit_multiplied_by_two % 10 + first_digit

            # remove the right most two digits from the credit card number
            number_to_process //= 100
        return 0 == sum % 10