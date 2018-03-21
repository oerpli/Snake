from ColorGenerator import *

class BlinkingColorGenerator(ColorGenerator):
    def __init__(self, color1 = "#f00", color2 = "#000"):
        self.colors = [color1, color2]
        self.currentColor = color1

    def getNextColor(self):
        if (self.currentColor == self.colors[0]):
            self.currentColor = self.colors[1]
        else:
            self.currentColor = self.colors[0]

        return self.currentColor