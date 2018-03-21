from abc import ABC, abstractmethod

class ColorGenerator(ABC):
    @abstractmethod
    def getNextColor(self):
        # returns a color as a hex string, e.g. "#FFF"
        pass