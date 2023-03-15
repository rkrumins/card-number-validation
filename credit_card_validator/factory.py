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
            LOGGER.error("Unable to load the implementation of {} algorithm, will default to {}".format(validator, DEFAULT_CARD_NUMBER_VALIDATOR))
            raise Exception("Unable to obtain the implementation of {} algorithm.".format(validator))
    except Exception as e:
        logging.exception(e)
        logging.error("Unable to load algorithm: {0}, defaulting to {1} algorithm".format(validator, DEFAULT_CARD_NUMBER_VALIDATOR))
        return LuhnValidator()
