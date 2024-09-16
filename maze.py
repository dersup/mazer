from drawing import *
from time import sleep
import random


class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win, seed=None):
        self.__tlcor = Point(x1, y1)
        self.__brcor = Point(win.x - x1, win.y - y1)
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__seed = 0 if not seed else random.seed(seed)
        self.cells = []

    def _create_cells(self):
        curr_y = self.__tlcor.y
        for i in range(self.__num_rows):
            curr_x = self.__tlcor.x
            self.cells.append([])
            for j in range(self.__num_cols):
                self.cells[i].append(Cell(self.__win, Point(curr_x, curr_y), Point(curr_x + self.__cell_size_x, curr_y + self.__cell_size_y)))
                self._draw_cell(i, j)
                curr_x += self.__cell_size_x
            curr_y += self.__cell_size_y

    def _draw_cell(self, i, j):
        self.cells[i][j].draw()
        self._animate()

    def _animate(self):
        self.__win.redraw()
        sleep(0.05)

    def break_ent_exit(self):
        self.cells[0][0].right = False
        self.cells[0][0].visited = True
        self.cells[0][0].draw()
        self.cells[-1][-1].left = False
        self.cells[-1][-1].visited = True
        self.cells[-1][-1].draw()

    def break_walls(self, i, j):
        self.cells[i][j].visited = True
        while 1:
            possibal = []
            picks = []
            if i > 0 and i < self.__num_rows - 1:
                possibal.extend([[i - 1, j], [i + 1, j]])
            elif i == 0:
                possibal.append([i + 1, j])
            elif i == self.__num_rows - 1:
                possibal.append([i - 1, j])
            if j > 0 and j < self.__num_cols - 1:
                possibal.extend([[i, j + 1], [i, j - 1]])
            elif j == 0:
                possibal.append([i, j + 1])
            elif j == self.__num_cols - 1:
                possibal.append([i, j - 1])
            for c in possibal:
                if not self.cells[c[0]][c[1]].visited:
                    picks.append(c)
            if len(picks) == 0:
                self._draw_cell(i, j)
                return
            pick = random.choice(picks)
            if pick[0] < i:
                self.cells[i][j].top = False
                self.cells[pick[0]][pick[1]].bottom = False
            elif pick[0] > i:
                self.cells[i][j].bottom = False
                self.cells[pick[0]][pick[1]].top = False
            if pick[1] > j:
                self.cells[i][j].right = False
                self.cells[pick[0]][pick[1]].left = False
            elif pick[1] < j:
                self.cells[i][j].left = False
                self.cells[pick[0]][pick[1]].right = False
            self.break_walls(pick[0], pick[1])

    def reset_visted(self):
        for row in self.cells:
            for cell in row:
                cell.visited = False

    def solve(self):
        return self.solve_r(0, 0)

    def solve_r(self, i, j):
        self._animate()
        self.cells[i][j].visited = True
        if i == self.__num_rows - 1 and j == self.__num_cols - 1:
            return True
        possibal = []
        if i > 0 and i < self.__num_rows - 1:
            if not self.cells[i][j].top:
                possibal.append([i - 1, j])
            if not self.cells[i][j].bottom:
                possibal.append([i + 1, j])
        elif i == 0:
            if not self.cells[i][j].bottom:
                possibal.append([i + 1, j])
        elif i == self.__num_rows - 1:
            if not self.cells[i][j].top:
                possibal.append([i - 1, j])
        if j > 0 and j < self.__num_cols - 1:
            if not self.cells[i][j].left:
                possibal.append([i, j - 1])
            if not self.cells[i][j].right:
                possibal.append([i, j + 1])
        elif j == 0:
            if not self.cells[i][j].right:
                possibal.append([i, j + 1])
        elif j == self.__num_cols - 1:
            if not self.cells[i][j].left:
                possibal.append([i, j - 1])
        for c in possibal:
            if not self.cells[c[0]][c[1]].visited:
                self.cells[i][j].move(self.cells[c[0]][c[1]])
                if self.solve_r(c[0], c[1]):
                    return True
                else:
                    self.cells[i][j].move(self.cells[c[0]][c[1]], True)
        return False
