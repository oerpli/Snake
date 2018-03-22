from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def keyPressed(self, event):
        pass