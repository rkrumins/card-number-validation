

class ConfigKeyConstants:
    MASK_CHARACTER_KEY_NAME = "MASK_CHARACTER"
    MASK_UNMASKED_DIGITS_COUNT_KEY_NAME = "MASK_UNMASKED_DIGITS_COUNT"
    VALIDATION_METHOD = "CARD_NUMBER_VALIDATION_ALGORITHM"


class InputPayloadModelConstants:
    CARD_NUMBER_FIELD_NAME = "card-number"


class ResponsePayloadFields:
    CARD_NUMBER_FIELD_NAME = "card-number"
    VALID_CARD_NUMBER_FIELD_NAME = "valid-card-number"
    VALIDATION_METHOD_FIELD_NAME = "validation-method"


class DefaultConstants:
    DEFAULT_CARD_NUMBER_VALIDATOR = "Luhn"
    DEFAULT_MASK_CHARACTER = "*"
    DEFAULT_UNMASKED_DIGITS_COUNT = 4
