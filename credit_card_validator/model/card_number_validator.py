from abc import ABCMeta, abstractmethod


class CardNumberValidator(metaclass=ABCMeta):
    def __init__(self) -> None:
        super().__init__()
    
    @abstractmethod
    def validate(self, number):
        raise NotImplementedError

