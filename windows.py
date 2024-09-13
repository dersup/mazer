from tkinter import Tk, BOTH, Canvas
from drawing import *


class Windows():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__root = Tk()
        self.__root.title("mazer")
        self.canvas = Canvas(self.__root, bg="black", height=y, width=x)
        self.canvas.pack()
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line, colour):
        line.draw(self.canvas, colour)
