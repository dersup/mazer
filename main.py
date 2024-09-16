from windows import *
from drawing import *
from maze import *


def Main():
    win = Windows(800, 800)
    maze1 = Maze(1, 1, 10, 10, 799 // 10, 799 // 10, win)
    maze1._create_cells()
    maze1.break_walls(0, 0)
    maze1.reset_visted()
    maze1.solve()
    win.wait_for_close()


Main()
