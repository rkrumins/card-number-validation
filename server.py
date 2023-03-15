import logging

from flask import Flask, jsonify
from credit_card_validator import factory
from credit_card_validator.utils import config_utils
from credit_card_validator.constants import ConfigKeyConstants, DEFAULT_CARD_NUMBER_VALIDATOR
from logging_config import LOGGING_CONFIG
from logging.config import dictConfig
import json
from flask.logging import default_handler

dictConfig(LOGGING_CONFIG)
app = Flask(__name__)

app_config = config_utils.load_config_from_local_filesystem("config/app_dev.yml")
logging.info("Application config is set to the following: {}".format(json.dumps(app_config)))

card_number_validator = factory.get_validator(app_config[ConfigKeyConstants.VALIDATION_METHOD])

@app.route("/validate/luhn/<string:card_number>", methods=["GET"])
def validate_credit_card(card_number):
    flag = card_number_validator.validate(card_number)

    # Uncommented for now but this might be required for data privacy reasons - especially in log files
    # masked_card_number = validation_utils.mask_credit_card_digits(
    #     card_number,
    #     app_config[ConfigKeyConstants.MASK_UNMASKED_DIGITS_COUNT_KEY_NAME],
    #     app_config[ConfigKeyConstants.MASK_CHARACTER_KEY_NAME]
    # )
    return jsonify({
        "card-number": card_number,
        "valid-card-number": flag,
        "validation-method": card_number_validator.get_name()
    })

