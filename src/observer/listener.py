from abc import ABC, abstractmethod

from .publisher import Publisher


class Listener(ABC):
    def __init__(self, name):
        """
        Method used as template and abstract class for the observer
        check this dock https://refactoring.guru/design-patterns/observer
        """
        self.name = name

    def subscribe(self, suscription: Publisher) -> None:
        suscription.atach(self)

    @abstractmethod
    def notify(self) -> None:
        raise NotImplementedError
