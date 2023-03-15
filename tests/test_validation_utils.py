from credit_card_validator.utils import validation_utils as object_under_test


def test_should_return_false_flag_for_empty_input():
    input_card_number = None
    valid_card_number_flag = object_under_test.get_valid_card_number_flag(input_card_number)
    assert valid_card_number_flag is False


def test_should_return_false_flag_for_non_numeric_characters():
    input_card_number = "abc"
    valid_card_number_flag = object_under_test.get_valid_card_number_flag(input_card_number)
    assert valid_card_number_flag is False


def test_should_return_false_flag_for_special_characters():
    input_card_number = ".,:'"
    valid_card_number_flag = object_under_test.get_valid_card_number_flag(input_card_number)
    assert valid_card_number_flag is False


def test_should_return_true_flag_for_valid_input_number():
    input_card_number = "49927398716"
    valid_card_number_flag = object_under_test.get_valid_card_number_flag(input_card_number)
    assert valid_card_number_flag is True


def test_should_parse_input_containing_whitespaces():
    input_card_number = "  49927398716  "
    actual_value = object_under_test.parse_input(input_card_number)
    expected_value = "49927398716"
    assert actual_value == expected_value


def test_should_mask_card_number():
    input_card_number = "5425233430109903"
    expected_masked_card_number = "************9903"
    actual_masked_card_number = object_under_test.mask_credit_card_digits(input_card_number, 4)
    assert actual_masked_card_number == expected_masked_card_number


def test_should_mask_card_number_with_whitespaces():
    input_card_number = "5425233430109903  "
    expected_masked_card_number = "************9903"
    actual_masked_card_number = object_under_test.mask_credit_card_digits(input_card_number, 4)
    assert actual_masked_card_number == expected_masked_card_number


def test_should_mask_card_number_with_multiple_whitespaces_and_characters():
    input_card_number = "  5425233  4301099  03  qz"
    expected_masked_card_number = "************9903"
    actual_masked_card_number = object_under_test.mask_credit_card_digits(input_card_number, 4)
    assert actual_masked_card_number == expected_masked_card_number


def test_should_return_only_mask_characters_if_card_number_is_shorter_than_unmasked_digits_count():
    input_card_number = "  5425233  4301099  03  qz"
    expected_masked_card_number = "****************"
    actual_masked_card_number = object_under_test.mask_credit_card_digits(input_card_number, 30)
    assert actual_masked_card_number == expected_masked_card_number


def test_should_return_only_mask_characters_if_card_number_is_shorter_than_unmasked_digits_count():
    input_card_number = "  5425233  4301099  03"
    expected_masked_card_number = "****************"
    actual_masked_card_number = object_under_test.mask_credit_card_digits(input_card_number, 0)
    assert actual_masked_card_number == expected_masked_card_number
