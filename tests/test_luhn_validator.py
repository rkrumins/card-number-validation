from credit_card_validator.validators.luhn_validator import LuhnValidator

object_under_test = LuhnValidator()


def test_should_throw_exception_for_null_input():
    input_card_number_value = None
    valid_number_flag = object_under_test.validate(input_card_number_value)
    assert valid_number_flag is False


def test_should_throw_exception_for_empty_input():
    input_card_number_value = ""
    valid_number_flag = object_under_test.validate(input_card_number_value)
    assert valid_number_flag is False


def test_should_throw_exception_for_multiple_input_spaces():
    input_card_number_value = "   "
    valid_number_flag = object_under_test.validate(input_card_number_value)
    assert valid_number_flag is False


def test_should_throw_exception_for_invalid_input_card_number_value():
    input_card_number_value = "123a"
    valid_number_flag = object_under_test.validate(input_card_number_value)
    assert valid_number_flag is False


def test_should_throw_exception_for_invalid_input_characters():
    input_card_number_value = "abc"
    valid_number_flag = object_under_test.validate(input_card_number_value)
    assert valid_number_flag is False


def test_should_return_true_for_valid_input_string():
    input_card_number_value = "49927398716"
    valid_number_flag = object_under_test.validate(input_card_number_value)
    assert valid_number_flag is True


def test_should_return_true_for_integer_input_card_number_value():
    input_card_number_value = 49927398716
    valid_number_flag = object_under_test.validate(input_card_number_value)
    assert valid_number_flag is True


def test_should_return_false_for_valid_input_string():
    input_card_number_value = "123"
    valid_number_flag = object_under_test.validate(input_card_number_value)
    assert valid_number_flag is False


def test_should_return_false_for_integer_input_card_number_value():
    input_card_number_value = 123
    valid_number_flag = object_under_test.validate(input_card_number_value)
    assert valid_number_flag is False


def test_should_return_false_for_integer_input_card_number_value():
    input_card_number_value = 123
    valid_number_flag = object_under_test.validate(input_card_number_value)
    assert valid_number_flag is False


def test_should_return_true_for_valid_input_string_with_single_space():
    input_card_number_values = [
        "499273 98716",
        " 49927398716",
        "49927398716 ",
    ]
    actual_results_list = [object_under_test.validate(input_card_number_value) for input_card_number_value in input_card_number_values]
    assert all(actual_results_list) is True


def test_should_return_true_for_valid_input_string_with_multiple_spaces():
    input_card_number_values = [
        "499   273  98716",
        "  4 9927 39  8716   ",
        "4 9 9  2 7 3 987 16 ",
    ]
    actual_results_list = [object_under_test.validate(input_card_number_value) for input_card_number_value in input_card_number_values]
    assert all(actual_results_list) is True


def test_should_return_true_for_very_large_integer_value():
    input_card_number = 6117329787959456170402582648081144717220758665842882823134765328921559889572988914329210134966229215
    actual_result_flag = object_under_test.validate(input_card_number)
    expected_result_flag = True
    assert actual_result_flag == expected_result_flag


def test_should_return_true_for_very_large_string_value():
    input_card_number = "6117329787959456170402582648081144717220758665842882823134765328921559889572988914329210134966229215"
    actual_result_flag = object_under_test.validate(input_card_number)
    expected_result_flag = True
    assert actual_result_flag == expected_result_flag

def test_should_return_false_for_very_large_integer_value_with_extra_invalid_characters():
    input_card_number = "abc6117329787959456170402582648081144717220758665842882823134765328921559889572988914329210134966229215  /."
    actual_result_flag = object_under_test.validate(input_card_number)
    expected_result_flag = False
    assert actual_result_flag == expected_result_flag
