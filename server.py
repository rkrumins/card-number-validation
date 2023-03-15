import logging

from flask import Flask, jsonify, request
from credit_card_validator import factory
from credit_card_validator.utils import config_utils, request_utils
from credit_card_validator.constants import ConfigKeyConstants, ResponsePayloadFields
from logging_config import LOGGING_CONFIG
from logging.config import dictConfig
import json

dictConfig(LOGGING_CONFIG)
app = Flask(__name__)

app_config = config_utils.load_config_from_local_filesystem("config/app_dev.yml")
logging.info("Application config is set to the following: {}".format(json.dumps(app_config)))

card_number_validator = factory.get_validator(app_config[ConfigKeyConstants.VALIDATION_METHOD])


# TODO: Deprecate below endpoint for real (outside world) application
@app.route("/validate/luhn/<string:card_number>", methods=["GET"])
def validate_credit_card(card_number):
    flag = card_number_validator.validate(card_number)

    # Uncommented for now but this might be required for data privacy reasons - especially in log files and return payloads in order to mask sensitive fields
    # masked_card_number = validation_utils.mask_credit_card_digits(
    #     card_number,
    #     app_config[ConfigKeyConstants.MASK_UNMASKED_DIGITS_COUNT_KEY_NAME],
    #     app_config[ConfigKeyConstants.MASK_CHARACTER_KEY_NAME]
    # )
    return jsonify({
        ResponsePayloadFields.CARD_NUMBER_FIELD_NAME: card_number,
        ResponsePayloadFields.VALID_CARD_NUMBER_FIELD_NAME: flag,
        ResponsePayloadFields.VALIDATION_METHOD_FIELD_NAME: card_number_validator.get_name()
    }), 200


@app.route("/validate/luhn", methods=["POST"])
def validate_credit_card_using_json_payload():
    content_type = request.headers.get("Content-Type")
    if content_type == "application/json":
        json_payload = request.get_json()
        card_number = request_utils.get_card_number_from_json(json_payload)
        if not card_number:
            return jsonify("""Invalid payload format, you must specify all the payload fields and those cannot be empty, e.g. { "card-number": "1234" }"""), 400
        flag = card_number_validator.validate(card_number)
        # Uncommented for now but this might be required for data privacy reasons - especially in log files and return payloads in order to mask sensitive fields
        # masked_card_number = validation_utils.mask_credit_card_digits(
        #     card_number,
        #     app_config[ConfigKeyConstants.MASK_UNMASKED_DIGITS_COUNT_KEY_NAME],
        #     app_config[ConfigKeyConstants.MASK_CHARACTER_KEY_NAME]
        # )
        # TODO: Return payload should return masked contents of card number for security reasons
        return jsonify({
            ResponsePayloadFields.CARD_NUMBER_FIELD_NAME: card_number,
            ResponsePayloadFields.VALID_CARD_NUMBER_FIELD_NAME: flag,
            ResponsePayloadFields.VALIDATION_METHOD_FIELD_NAME: card_number_validator.get_name()
        }), 200
    else:
        return jsonify("Content-Type not supported! You must specify a valid JSON request body payload"), 400

