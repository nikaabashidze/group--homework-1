from abc import ABC, abstractmethod


class Factory(ABC):
    @abstractmethod
    def description(self):
        pass

    @abstractmethod
    def validate(self):
        pass

    