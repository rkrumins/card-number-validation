from credit_card_validator.utils import validation_utils
from credit_card_validator.validators.luhn_validator import LuhnValidator
from credit_card_validator.constants import DefaultConstants
import logging

LOGGER = logging.getLogger(__name__)


def get_validator(validator=DefaultConstants.DEFAULT_CARD_NUMBER_VALIDATOR):
    try:
        validation_method = validator.lower()
        validation_method = validation_utils.parse_input(validation_method)
        if validation_method == "luhn":
            LOGGER.info("Card numbers will be validated using Luhn algorithm")
            return LuhnValidator()
        else:
            exception_message = "Unable to obtain the implementation of {0} algorithm as per the configuration file".format(validator)
            LOGGER.error(exception_message)
            raise Exception(exception_message)
    except Exception as e:
        LOGGER.info("Loading default validation algorithm: {0}".format(DefaultConstants.DEFAULT_CARD_NUMBER_VALIDATOR))
        return LuhnValidator()
