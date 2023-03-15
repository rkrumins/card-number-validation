from abc import ABCMeta, abstractmethod


class CardNumberValidator(metaclass=ABCMeta):
    def __init__(self) -> None:
        super().__init__()

    @property
    @abstractmethod
    def get_name(self):
        raise NotImplementedError

    @abstractmethod
    def validate(self, number):
        raise NotImplementedError

