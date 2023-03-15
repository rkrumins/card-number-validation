import credit_card_validator.utils.request_utils as object_under_test

def test_should_return_card_number_value_from_input_payload():
    input_payload = {"card-number": "1234"}
    expected_card_number = "1234"
    actual_card_number = object_under_test.get_card_number_from_json(input_payload)
    assert actual_card_number == expected_card_number


def test_should_return_none_for_empty_required_key_value():
    input_payload = {"card-number": ""}
    expected_card_number = None
    actual_card_number = object_under_test.get_card_number_from_json(input_payload)
    assert actual_card_number == expected_card_number


def test_should_return_none_for_unspecified_required_key_value():
    input_payload = {"card-number"}
    expected_card_number = None
    actual_card_number = object_under_test.get_card_number_from_json(input_payload)
    assert actual_card_number == expected_card_number


def test_should_return_none_for_invalid_json_payload_fields():
    input_payload = {"some-random-field": "12345"}
    expected_card_number = None
    actual_card_number = object_under_test.get_card_number_from_json(input_payload)
    assert actual_card_number == expected_card_number


def test_should_return_none_for_empty_request_payload():
    input_payload = {}
    expected_card_number = None
    actual_card_number = object_under_test.get_card_number_from_json(input_payload)
    assert actual_card_number == expected_card_number


def test_should_return_card_number_value_from_input_payload_as_integer():
    input_payload = {"card-number": 1234}
    expected_card_number = 1234
    actual_card_number = object_under_test.get_card_number_from_json(input_payload)
    assert actual_card_number == expected_card_number
