class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Line():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, colour):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=colour, width=2)


class Cell():
    def __init__(self, window, top_corner, bottom_corner, top=True, bottom=True, left=True, right=True):
        self.__tlcor = top_corner
        self.__brcor = bottom_corner
        self.__trcor = Point(self.__brcor.x, self.__tlcor.y)
        self.__blcor = Point(self.__tlcor.x, self.__brcor.y)
        self.__cent = Point((self.__trcor.x - self.__tlcor.x) / 2 + self.__tlcor.x, (self.__brcor.y - self.__trcor.y) / 2 + self.__trcor.y)
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right
        self.__win = window
        self.visited = False

    def draw(self):
        if self.top:
            self.__win.draw_line(Line(self.__trcor, self.__tlcor), "white")
        else:
            self.__win.draw_line(Line(self.__trcor, self.__tlcor), "black")
        if self.bottom:
            self.__win.draw_line(Line(self.__brcor, self.__blcor), "white")
        else:
            self.__win.draw_line(Line(self.__brcor, self.__blcor), "black")
        if self.left:
            self.__win.draw_line(Line(self.__tlcor, self.__blcor), "white")
        else:
            self.__win.draw_line(Line(self.__tlcor, self.__blcor), "black")
        if self.right:
            self.__win.draw_line(Line(self.__brcor, self.__trcor), "white")
        else:
            self.__win.draw_line(Line(self.__brcor, self.__trcor), "black")

    def move(self, to_cell, undo=False):
        colour = "grey"
        if undo:
            colour = "red"
        self.__win.draw_line(Line(self.__cent, to_cell.__cent), colour)
