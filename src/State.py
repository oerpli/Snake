from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def keyPressed(self, event):
        pass