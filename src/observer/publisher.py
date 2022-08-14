from .listener import Listener


class Publisher:
    """
    Method used to notifiy other classes when something happend
    check this doc https://refactoring.guru/design-patterns/observer
    """

    def __init__(self, stack):
        self.stack = stack
        self.listeners: list = []

    def notify(self) -> None:
        for listener in self.listeners:
            listener.notify()

    def atach(self, listener: Listener) -> None:
        self.listeners.append(listener)
