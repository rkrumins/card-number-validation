import logging
from credit_card_validator.model.card_number_validator import CardNumberValidator
from credit_card_validator.utils import validation_utils

LOGGER = logging.getLogger(__name__)

class LuhnValidator(CardNumberValidator):

    def __init__(self):
        super().__init__()
        self._name = "Luhn"

    def get_name(self):
        return self._name

    def validate(self, number) -> bool:
        try:
            parsed_credit_card_number = validation_utils.parse_input(number)
            valid_credit_number_flag = validation_utils.get_valid_card_number_flag(parsed_credit_card_number)

            if not valid_credit_number_flag:
                LOGGER.error("Invalid input provided, therefore the number {} is not a valid card number as per Luhn algorithm".format(parsed_credit_card_number))
                return False

            parsed_credit_card_number_reversed = parsed_credit_card_number[::-1]

            credit_card_number_digits_list = validation_utils.get_credit_card_number_digits_list(parsed_credit_card_number_reversed)
            checksum = 0

            for digit_index in range(0, len(credit_card_number_digits_list)):
                if digit_index % 2 == 1:
                    digit = credit_card_number_digits_list[digit_index]
                    digit_product = digit * 2

                    if digit_product > 9:
                        checksum += digit_product % 10 + 1
                    else:
                        checksum += digit_product
                else:
                    checksum += credit_card_number_digits_list[digit_index]

            if checksum % 10 == 0:
                LOGGER.info("The number {} is a valid card number as per Luhn algorithm given that checksum is valid".format(parsed_credit_card_number))
                return True
            else:
                LOGGER.error("The number {} is NOT a valid card number as per Luhn algorithm given that checksum is invalid".format(number))
                return False

        except Exception as ex:
            LOGGER.error("Invalid credit card number provided for input: {}".format(number))
            LOGGER.exception(ex, exc_info=True)

        return False
