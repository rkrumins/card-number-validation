from credit_card_validator.utils import validation_utils
from credit_card_validator.validators.luhn_validator import LuhnValidator
from credit_card_validator.constants import DEFAULT_CARD_NUMBER_VALIDATOR
import logging

LOGGER = logging.getLogger(__name__)


def get_validator(validator=DEFAULT_CARD_NUMBER_VALIDATOR):
    try:
        validation_method = validator.lower()
        validation_method = validation_utils.parse_input(validation_method)
        if validation_method == "luhn":
            LOGGER.info("Card numbers will be validated using Luhn algorithm")
            return LuhnValidator()
        else:
            LOGGER.error("Unable to load the implementation of {0} algorithm, will default to {1}".format(validator, DEFAULT_CARD_NUMBER_VALIDATOR))
            exception_message = "Unable to obtain the implementation of {0} algorithm".format(validator)
            raise Exception(exception_message)
    except Exception as e:
        LOGGER.exception(e)
        LOGGER.error("Unable to load algorithm: {0}, defaulting to {1} algorithm".format(validator, DEFAULT_CARD_NUMBER_VALIDATOR))
        return LuhnValidator()
