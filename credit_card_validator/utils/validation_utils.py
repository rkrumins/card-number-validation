import logging

from credit_card_validator.constants import DefaultConstants
from credit_card_validator.exceptions import InvalidInputValueException, EmptyInputValueException
import regex as re
re.DEFAULT_VERSION = re.VERSION1

LOGGER = logging.getLogger(__name__)


def get_credit_card_number_digits_list(credit_card_number_str: str) -> list:
    if credit_card_number_str:
        credit_card_number_digits_list = [int(digit) for digit in credit_card_number_str]
        return credit_card_number_digits_list
    return list()


def get_valid_card_number_flag(input_number) -> bool:
    if input_number:
        try:
            valid_digit_flags_list = [digit_character.isdigit() for digit_character in input_number]
            valid_numbers_flag = all(valid_digit_flags_list)
            LOGGER.debug("The number {} appears to be a valid card number".format(input_number))
            return valid_numbers_flag
        except Exception:
            LOGGER.error("The number: {} is not a valid number".format(input_number))
            raise InvalidInputValueException("Invalid card number passed")
    return False


def parse_input(input_string) -> str:
    if input_string:
        try:
            input_string = str(input_string).strip().replace(" ", "")
            if input_string:
                return input_string
            else:
                raise EmptyInputValueException("Empty input passed")
        except ValueError as ex:
            LOGGER.exception("Invalid input passed", ex)
            raise Exception("Unable to parse credit card number") from ex
    raise EmptyInputValueException("Empty input passed")


# Not in use at the moment but could be helpful when returning the output to user
def mask_credit_card_digits(full_credit_card_number, unmasked_digits_count=DefaultConstants.DEFAULT_UNMASKED_DIGITS_COUNT, mask_character=DefaultConstants.DEFAULT_MASK_CHARACTER):
    full_credit_card_number_clean = ''.join(i for i in str(full_credit_card_number) if i.isdigit())

    full_credit_card_number_length = len(full_credit_card_number_clean)

    if full_credit_card_number_length < 15:
        # Given that AMEX number count is minimum 15 and for VISA/Mastercard it is 16
        LOGGER.warning("Card number length is less the standard, expected, count")
    elif unmasked_digits_count > 4:
        LOGGER.warning("Unmasked card numbers count should not be more than 4 by default")
        # Unmasked digits count should be set to default figure, e.g. 4 for standard car numbers, thus enforced
        # unmasked_digits_count = 4

    if full_credit_card_number_length <= unmasked_digits_count:
        LOGGER.debug("Returning full masked card number")
        return mask_character * full_credit_card_number_length

    masked_digits_count = full_credit_card_number_length - unmasked_digits_count
    mask_substring = mask_character * masked_digits_count
    unmasked_characters_range = full_credit_card_number_length - unmasked_digits_count

    masked_card_number = "{}{}".format(mask_substring, full_credit_card_number_clean[unmasked_characters_range:full_credit_card_number_length])
    LOGGER.info("Masked card number is: {}".format(masked_card_number))
    return masked_card_number
