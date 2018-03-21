from ColorGenerator import *

class SingleColorGenerator(ColorGenerator):
    def __init__(self, color = "#000"):
        self.color = color

    def getNextColor(self):
        return self.color