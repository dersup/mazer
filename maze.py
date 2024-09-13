from drawing import *
from time import sleep


class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win,):
        self.__tlcor = Point(x1, y1)
        self.__brcor = Point(win.x - x1, win.y - y1)
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.cells = []

    def _create_cells(self):
        curr_y = self.__tlcor.y
        for i in range(self.__num_rows):
            curr_x = self.__tlcor.x
            self.cells.append([])
            for j in range(self.__num_cols):
                self.cells[i].append(Cell(self.__win, Point(curr_x, curr_y), Point(curr_x + self.__cell_size_x, curr_y + self.__cell_size_y)))
                self._draw_cell()
                curr_x += self.__cell_size_x
            curr_y += self.__cell_size_y

    def _draw_cell(self):
        self.cells[-1][-1].draw()
        self._animate()

    def _animate(self):
        self.__win.redraw()
        sleep(0.05)

    def break_ent_exit(self):
        self.cells[0][0].right = False
        print(self.cells[0][0]._Cell__trcor.x, self.cells[0][0]._Cell__brcor.x)
        self.cells[0][0].draw()
        self.cells[-1][-1].left = False
        self.cells[-1][-1].draw()
