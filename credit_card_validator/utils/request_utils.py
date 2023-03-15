import logging

from credit_card_validator.constants import InputPayloadModelConstants

LOGGER = logging.getLogger(__name__)


def get_card_number_from_json(request_payload):
    if not request_payload:
        LOGGER.error("Empty payload provided")
    elif type(request_payload) is not dict:
        LOGGER.error("Invalid JSON payload provided")
    elif InputPayloadModelConstants.CARD_NUMBER_FIELD_NAME not in request_payload or not request_payload[InputPayloadModelConstants.CARD_NUMBER_FIELD_NAME]:
        LOGGER.error("""Invalid payload format provided, you must define valid payload format providing following fields e.g. { "card-number" : "1234" }""")
    else:
        # At the moment validation of field contents is not included at extraction of card number since that is done by each validator automatically
        return request_payload[InputPayloadModelConstants.CARD_NUMBER_FIELD_NAME]
    return None
