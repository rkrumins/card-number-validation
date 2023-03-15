import logging_config
from credit_card_validator import factory
import argparse
from logging.config import dictConfig

LOGGER = dictConfig(logging_config.LOGGING_CONFIG)


# def parse_args():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--algorithm', type=str, required=True)
#     parser.add_argument('--card_number', type=str, required=True)
#     args = parser.parse_args()
#     return args


if __name__ == "__main__":
    # args = parse_args()
    # algorithm = args.algorithm
    # card_number = args.card_number
    algorithm = "luhn"
    card_number = "123"
    validator = factory.get_validator(algorithm)
    result_flag = validator.validate(card_number)
    print(result_flag)
