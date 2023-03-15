# Custom exceptions module

class EmptyInputValueException(Exception):
    pass


class InvalidInputValueException(Exception):
    pass


class ConfigFileNotFoundException(FileNotFoundError):
    pass