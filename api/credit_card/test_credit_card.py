from unittest import TestCase
from .models import CreditCard
from .credit_card_manager import CreditCardManager

class BaseTest(TestCase):
    def setUp(self):
        self.credit_card_service = CreditCardManager()

class AmericanExpressCreditCardTest(BaseTest):
    pass

    def test_valid_american_express_credit_card_34(self):
        valid_credit_card = self.credit_card_service.parse_credit_card('341234568898772')

        # verify all major components of the american express card were properly parsed
        self.assertEqual(valid_credit_card.major_industry_identifier, 3)
        self.assertEqual(valid_credit_card.issuer_identification_number, 34)
        self.assertEqual(valid_credit_card.personal_account_number, 123456889877)
        self.assertEqual(valid_credit_card.check_digit, 2)
        self.assertEqual(self.credit_card_service.validate_credit_card(valid_credit_card), True)

    def test_valid_american_express_credit_card_37(self):
        valid_credit_card = self.credit_card_service.parse_credit_card('371234567898339')

        # verify all major components of the american express card were properly parsed
        self.assertEqual(valid_credit_card.major_industry_identifier, 3)
        self.assertEqual(valid_credit_card.issuer_identification_number, 37)
        self.assertEqual(valid_credit_card.personal_account_number, 123456789833)
        self.assertEqual(valid_credit_card.check_digit, 9)
        self.assertEqual(self.credit_card_service.validate_credit_card(valid_credit_card), True)

    def test_invalid_american_express_iin(self):
        invalid_credit_card = self.credit_card_service.parse_credit_card('141234567898769')

        # verify identification number is set to zero
        self.assertEqual(invalid_credit_card.issuer_identification_number, 0)
        self.assertEqual(self.credit_card_service.validate_credit_card(invalid_credit_card), False)

class DiscoverCreditCardTest(BaseTest):
    pass

    def test_valid_discover_credit_card_64(self):
        valid_credit_card = self.credit_card_service.parse_credit_card('6412345678947399')

        # verify all major components of the american express card were properly parsed
        self.assertEqual(valid_credit_card.major_industry_identifier, 6)
        self.assertEqual(valid_credit_card.issuer_identification_number, 64)
        self.assertEqual(valid_credit_card.personal_account_number, 1234567894739)
        self.assertEqual(valid_credit_card.check_digit, 9)
        self.assertEqual(self.credit_card_service.validate_credit_card(valid_credit_card), True)

    def test_valid_discover_credit_card_65(self):
        valid_credit_card = self.credit_card_service.parse_credit_card('65123456789838959')

        # verify all major components of the american express card were properly parsed
        self.assertEqual(valid_credit_card.major_industry_identifier, 6)
        self.assertEqual(valid_credit_card.issuer_identification_number, 65)
        self.assertEqual(valid_credit_card.personal_account_number, 12345678983895)
        self.assertEqual(valid_credit_card.check_digit, 9)
        self.assertEqual(self.credit_card_service.validate_credit_card(valid_credit_card), True)

    def test_valid_discover_credit_card_6011(self):
        valid_credit_card = self.credit_card_service.parse_credit_card('60113486789876959')

        # verify all major components of the american express card were properly parsed
        self.assertEqual(valid_credit_card.major_industry_identifier, 6)
        self.assertEqual(valid_credit_card.issuer_identification_number, 6011)
        self.assertEqual(valid_credit_card.personal_account_number, 348678987695)
        self.assertEqual(valid_credit_card.check_digit, 9)
        self.assertEqual(self.credit_card_service.validate_credit_card(valid_credit_card), True)

    def test_valid_discover_credit_card_622126(self):
        valid_credit_card = self.credit_card_service.parse_credit_card('62212656989896959')

        # verify all major components of the american express card were properly parsed
        self.assertEqual(valid_credit_card.major_industry_identifier, 6)
        self.assertEqual(valid_credit_card.issuer_identification_number, 622126)
        self.assertEqual(valid_credit_card.personal_account_number, 5698989695)
        self.assertEqual(valid_credit_card.check_digit, 9)
        self.assertEqual(self.credit_card_service.validate_credit_card(valid_credit_card), True)

    def test_valid_discover_credit_card_622925(self):
        valid_credit_card = self.credit_card_service.parse_credit_card('62292556789866959')

        # verify all major components of the american express card were properly parsed
        self.assertEqual(valid_credit_card.major_industry_identifier, 6)
        self.assertEqual(valid_credit_card.issuer_identification_number, 622925)
        self.assertEqual(valid_credit_card.personal_account_number, 5678986695)
        self.assertEqual(valid_credit_card.check_digit, 9)
        self.assertEqual(self.credit_card_service.validate_credit_card(valid_credit_card), True)

    def test_valid_discover_credit_card_622923(self):
        valid_credit_card = self.credit_card_service.parse_credit_card('6229239678987695959')

        # verify all major components of the american express card were properly parsed
        self.assertEqual(valid_credit_card.major_industry_identifier, 6)
        self.assertEqual(valid_credit_card.issuer_identification_number, 622923)
        self.assertEqual(valid_credit_card.personal_account_number, 967898769595)
        self.assertEqual(valid_credit_card.check_digit, 9)
        self.assertEqual(self.credit_card_service.validate_credit_card(valid_credit_card), True)

    def test_valid_discover_credit_card_624000(self):
        valid_credit_card = self.credit_card_service.parse_credit_card('62400056789866959')

        # verify all major components of the american express card were properly parsed
        self.assertEqual(valid_credit_card.major_industry_identifier, 6)
        self.assertEqual(valid_credit_card.issuer_identification_number, 624000)
        self.assertEqual(valid_credit_card.personal_account_number, 5678986695)
        self.assertEqual(valid_credit_card.check_digit, 9)
        self.assertEqual(self.credit_card_service.validate_credit_card(valid_credit_card), True)

    def test_valid_discover_credit_card_626999(self):
        valid_credit_card = self.credit_card_service.parse_credit_card('62699956789876959')

        # verify all major components of the american express card were properly parsed
        self.assertEqual(valid_credit_card.major_industry_identifier, 6)
        self.assertEqual(valid_credit_card.issuer_identification_number, 626999)
        self.assertEqual(valid_credit_card.personal_account_number, 5678987695)
        self.assertEqual(valid_credit_card.check_digit, 9)
        self.assertEqual(self.credit_card_service.validate_credit_card(valid_credit_card), True)

    def test_valid_discover_credit_card_626998(self):
        valid_credit_card = self.credit_card_service.parse_credit_card('62699856789896959')

        # verify all major components of the american express card were properly parsed
        self.assertEqual(valid_credit_card.major_industry_identifier, 6)
        self.assertEqual(valid_credit_card.issuer_identification_number, 626998)
        self.assertEqual(valid_credit_card.personal_account_number, 5678989695)
        self.assertEqual(valid_credit_card.check_digit, 9)
        self.assertEqual(self.credit_card_service.validate_credit_card(valid_credit_card), True)

    def test_valid_discover_credit_card_628200(self):
        valid_credit_card = self.credit_card_service.parse_credit_card('62820056789886959')

        # verify all major components of the american express card were properly parsed
        self.assertEqual(valid_credit_card.major_industry_identifier, 6)
        self.assertEqual(valid_credit_card.issuer_identification_number, 628200)
        self.assertEqual(valid_credit_card.personal_account_number, 5678988695)
        self.assertEqual(valid_credit_card.check_digit, 9)
        self.assertEqual(self.credit_card_service.validate_credit_card(valid_credit_card), True)

    def test_valid_discover_credit_card_628899(self):
        valid_credit_card = self.credit_card_service.parse_credit_card('62889956789876959')

        # verify all major components of the american express card were properly parsed
        self.assertEqual(valid_credit_card.major_industry_identifier, 6)
        self.assertEqual(valid_credit_card.issuer_identification_number, 628899)
        self.assertEqual(valid_credit_card.personal_account_number, 5678987695)
        self.assertEqual(valid_credit_card.check_digit, 9)
        self.assertEqual(self.credit_card_service.validate_credit_card(valid_credit_card), True)

    def test_valid_discover_credit_card_628898(self):
        valid_credit_card = self.credit_card_service.parse_credit_card('62889856789896959')

        # verify all major components of the american express card were properly parsed
        self.assertEqual(valid_credit_card.major_industry_identifier, 6)
        self.assertEqual(valid_credit_card.issuer_identification_number, 628898)
        self.assertEqual(valid_credit_card.personal_account_number, 5678989695)
        self.assertEqual(valid_credit_card.check_digit, 9)
        self.assertEqual(self.credit_card_service.validate_credit_card(valid_credit_card), True)


    def test_invalid_discover_iin(self):
        invalid_credit_card = self.credit_card_service.parse_credit_card('628900567898769')

        # verify identification number is set to zero
        self.assertEqual(invalid_credit_card.issuer_identification_number, 0)
        self.assertEqual(self.credit_card_service.validate_credit_card(invalid_credit_card), False)

class MastercardCreditCardTest(BaseTest):
    pass

    def test_valid_mastercard_credit_card_51(self):
        valid_credit_card = self.credit_card_service.parse_credit_card('5112345678987499')

        # verify all major components of the american express card were properly parsed
        self.assertEqual(valid_credit_card.major_industry_identifier, 5)
        self.assertEqual(valid_credit_card.issuer_identification_number, 51)
        self.assertEqual(valid_credit_card.personal_account_number, 1234567898749)
        self.assertEqual(valid_credit_card.check_digit, 9)
        self.assertEqual(self.credit_card_service.validate_credit_card(valid_credit_card), True)

    def test_valid_mastercard_credit_card_54(self):
        valid_credit_card = self.credit_card_service.parse_credit_card('5412349678987399')

        # verify all major components of the american express card were properly parsed
        self.assertEqual(valid_credit_card.major_industry_identifier, 5)
        self.assertEqual(valid_credit_card.issuer_identification_number, 54)
        self.assertEqual(valid_credit_card.personal_account_number, 1234967898739)
        self.assertEqual(valid_credit_card.check_digit, 9)
        self.assertEqual(self.credit_card_service.validate_credit_card(valid_credit_card), True)

    def test_valid_mastercard_credit_card_55(self):
        valid_credit_card = self.credit_card_service.parse_credit_card('5512346678987899')

        # verify all major components of the american express card were properly parsed
        self.assertEqual(valid_credit_card.major_industry_identifier, 5)
        self.assertEqual(valid_credit_card.issuer_identification_number, 55)
        self.assertEqual(valid_credit_card.personal_account_number, 1234667898789)
        self.assertEqual(valid_credit_card.check_digit, 9)
        self.assertEqual(self.credit_card_service.validate_credit_card(valid_credit_card), True)

    def test_valid_mastercard_credit_card_2221(self):
        valid_credit_card = self.credit_card_service.parse_credit_card('2221347678987599')

        # verify all major components of the american express card were properly parsed
        self.assertEqual(valid_credit_card.major_industry_identifier, 2)
        self.assertEqual(valid_credit_card.issuer_identification_number, 2221)
        self.assertEqual(valid_credit_card.personal_account_number, 34767898759)
        self.assertEqual(valid_credit_card.check_digit, 9)
        self.assertEqual(self.credit_card_service.validate_credit_card(valid_credit_card), True)

    def test_valid_mastercard_credit_card_2720(self):
        valid_credit_card = self.credit_card_service.parse_credit_card('2720348678987999')

        # verify all major components of the american express card were properly parsed
        self.assertEqual(valid_credit_card.major_industry_identifier, 2)
        self.assertEqual(valid_credit_card.issuer_identification_number, 2720)
        self.assertEqual(valid_credit_card.personal_account_number, 34867898799)
        self.assertEqual(valid_credit_card.check_digit, 9)
        self.assertEqual(self.credit_card_service.validate_credit_card(valid_credit_card), True)

    def test_valid_mastercard_credit_card_2719(self):
        valid_credit_card = self.credit_card_service.parse_credit_card('2719349678988899')

        # verify all major components of the american express card were properly parsed
        self.assertEqual(valid_credit_card.major_industry_identifier, 2)
        self.assertEqual(valid_credit_card.issuer_identification_number, 2719)
        self.assertEqual(valid_credit_card.personal_account_number, 34967898889)
        self.assertEqual(valid_credit_card.check_digit, 9)
        self.assertEqual(self.credit_card_service.validate_credit_card(valid_credit_card), True)

    def test_invalid_mastercard_iin(self):
        invalid_credit_card = self.credit_card_service.parse_credit_card('561234567898769')

        # verify identification number is set to zero
        self.assertEqual(invalid_credit_card.issuer_identification_number, 0)
        self.assertEqual(self.credit_card_service.validate_credit_card(invalid_credit_card), False)

class VisaCreditCardTest(BaseTest):
    pass

    def test_valid_visa_credit_card_4(self):
        valid_credit_card = self.credit_card_service.parse_credit_card('4412345678997969')

        # verify all major components of the american express card were properly parsed
        self.assertEqual(valid_credit_card.major_industry_identifier, 4)
        self.assertEqual(valid_credit_card.issuer_identification_number, 4)
        self.assertEqual(valid_credit_card.personal_account_number, 41234567899796)
        self.assertEqual(valid_credit_card.check_digit, 9)
        self.assertEqual(self.credit_card_service.validate_credit_card(valid_credit_card), True)

    def test_valid_visa_credit_card_4571(self):
        valid_credit_card = self.credit_card_service.parse_credit_card('4571345678985599')

        # verify all major components of the american express card were properly parsed
        self.assertEqual(valid_credit_card.major_industry_identifier, 4)
        self.assertEqual(valid_credit_card.issuer_identification_number, 4571)
        self.assertEqual(valid_credit_card.personal_account_number, 34567898559)
        self.assertEqual(valid_credit_card.check_digit, 9)
        self.assertEqual(self.credit_card_service.validate_credit_card(valid_credit_card), True)

class GeneralCreditCardTests(BaseTest):
    pass

    def test_zero_credit_card_number(self):
        invalid_credit_card = self.credit_card_service.parse_credit_card('0')

        self.assertEqual(self.credit_card_service.validate_credit_card(invalid_credit_card), False)

    def test_empty_account_number(self):
        invalid_credit_card = self.credit_card_service.parse_credit_card('')

        self.assertEqual(self.credit_card_service.validate_credit_card(invalid_credit_card), False)

    def test_large_account_number(self):
        invalid_credit_card = self.credit_card_service.parse_credit_card('999999999999999999999999999999999999999999999')

        self.assertEqual(self.credit_card_service.validate_credit_card(invalid_credit_card), False)

    def test_card_number_with_spaces(self):
        invalid_credit_card = self.credit_card_service.parse_credit_card('3718 892513 11442')

        self.assertEqual(self.credit_card_service.validate_credit_card(invalid_credit_card), True)

    def test_card_number_with_dashes(self):
        invalid_credit_card = self.credit_card_service.parse_credit_card('3718-892513-11442')

        self.assertEqual(self.credit_card_service.validate_credit_card(invalid_credit_card), True)

    def test_generate_visa(self):
        visa_number = self.credit_card_service.generate_visa()

        self.assertTrue(self.credit_card_service.validate_credit_card(visa_number))

    def test_generate_mastercard(self):
        mastercard_number = self.credit_card_service.generate_mastercard()

        self.assertTrue(self.credit_card_service.validate_credit_card(mastercard_number))

    def test_generate_discover(self):
        discover_number = self.credit_card_service.generate_discover()

        self.assertTrue(self.credit_card_service.validate_credit_card(discover_number))

    def test_generate_american_express(self):
        american_express_number = self.credit_card_service.generate_american_express()

        self.assertTrue(self.credit_card_service.validate_credit_card(american_express_number))