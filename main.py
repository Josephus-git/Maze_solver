from window import Window, Point, Line
from cell_unit import Cell
from maze import Maze


def main():
    width, height = 800, 600
    win = Window(width, height+100)
    margin_x, margin_y = 50, 50
    num_row, num_col = 10, 20
    cell_size_x, cell_size_y = (width - (2*margin_x))/num_col , (height - (2*margin_y))/num_row
    
    c_maze = Maze(margin_x, margin_y, num_row, num_col, cell_size_x, cell_size_y, win)
    c_maze.solve()
    win.wait_for_close()

main()