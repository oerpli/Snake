import tkinter as tk
from collections import deque
import time

class SnakeGameView:
    SNAKE_WIDTH = 20
    REDRAW_DELAY = round(1000/60) # 60FPS

    def __init__(self):
        self.window = tk.Tk()
        self.canvas = tk.Canvas(self.window, bg="grey", height=250, width=300)

        snakeRects = [(0,0),(0,1),(0,2),(1,2),(2,2)]
        self.drawSnake(snakeRects)

        self.addPoint((3,2), 'RIGHT')
        
        self.canvas.pack()

        self.window.bind_all("<Key>", self.keyPressed)
        # self.window.bind_all("<KeyRelease>", self.keyReleased)
        self.window.after(SnakeGameView.REDRAW_DELAY, self.animate) 
        self.window.mainloop()

    def drawSnake(self, points):
        for rect in points:
            x = rect[0] * SnakeGameView.SNAKE_WIDTH
            y = rect[1] * SnakeGameView.SNAKE_WIDTH
            self.currentRect = self.canvas.create_rectangle(x, y, x + SnakeGameView.SNAKE_WIDTH, y + SnakeGameView.SNAKE_WIDTH, fill="black")

    def addPoint(self, point, drawingDirection):
        x = point[0] * SnakeGameView.SNAKE_WIDTH
        y = point[1] * SnakeGameView.SNAKE_WIDTH

        self.currentRect = self.canvas.create_rectangle(x, y, x + SnakeGameView.SNAKE_WIDTH, y + SnakeGameView.SNAKE_WIDTH, fill="black")

        self.change = SnakeGameView.SNAKE_WIDTH *1
        self.startTime = int(round(time.time()*1000)) 
        self.startValue = x
        self.easingDuration = 1000

    def animate(self):
        if (self.currentRect is not None): 
            currentTime = int(round(time.time()*1000))
            currentDuration = currentTime - self.startTime

            animationProgress = currentDuration / self.easingDuration

            coords = self.canvas.coords(self.currentRect)
            coords[2] = self.startValue + self.change * animationProgress

            self.canvas.coords(self.currentRect, coords)

            if (animationProgress >= 1.0):
                self.currentRect = None

        self.window.after(SnakeGameView.REDRAW_DELAY, self.animate)

    def keyPressed(self, event):
        if (event.keysym == 'Right'):
            self.moveDirX = 2
            self.moveDirY = 0
        elif (event.keysym == 'Left'):
            self.moveDirX = -2
            self.moveDirY = 0

    # def keyReleased(self, event):
        # self.moveDirX = 0
        # self.moveDirY = 0

a = SnakeGameView()
