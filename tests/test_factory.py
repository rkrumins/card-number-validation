import credit_card_validator.factory as object_under_test
from credit_card_validator.validators.luhn_validator import LuhnValidator


def test_should_load_default_implementation_of_validator_if_invalid_value_passed():
    validator = object_under_test.get_validator("MagicValidator")
    assert isinstance(validator, LuhnValidator)


def test_should_load_correct_implementation_of_validator_if_correct_value_passed():
    validator = object_under_test.get_validator("Luhn")
    assert isinstance(validator, LuhnValidator)
