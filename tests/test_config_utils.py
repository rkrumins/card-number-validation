from pytest import raises
import credit_card_validator.utils.config_utils as object_under_test
from credit_card_validator.exceptions import ConfigFileNotFoundException


def test_should_load_valid_yaml_file_successfully():
    test_config_file_path = "test_data/test_config.yml"
    test_config_file_contents = object_under_test.load_config_from_local_filesystem(test_config_file_path)
    assert test_config_file_contents["MASK_UNMASKED_DIGITS_COUNT"] == 4

def test_should_raise_file_not_found_exception_for_invalid_input_path():
    test_config_file_path = "test_data/non_existant_path.yml"
    with raises(ConfigFileNotFoundException):
        object_under_test.load_config_from_local_filesystem(test_config_file_path)
