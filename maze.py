from cell_unit import Cell

from window import Point

import time

import random


class Maze:
    def __init__(
            self, x1, y1,
            num_rows, num_cols,
            cell_size_x, cell_size_y, 
            win=None, test=False,
            seed=None
    ):
        self.x1, self.y1 = x1, y1
        self.num_rows, self.num_cols = num_rows, num_cols
        self.cell_size_x, self.cell_size_y = cell_size_x, cell_size_y
        self.__win, self.test = win, test
        if seed is not None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if [i, j] == [(self.num_rows-1), self.num_cols-1]:
            return True
        

        if j < self.num_cols-1:
            if not self._cells[i][j+1].has_left_wall and not self._cells[i][j+1].visited:
                self._cells[i][j].draw_move(self._cells[i][j+1])
                result_of_inner = self._solve_r(i, j+1)
                if result_of_inner:
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i][j+1], True)

        if j > 0:
            if not self._cells[i][j-1].has_right_wall and not self._cells[i][j-1].visited:
                self._cells[i][j].draw_move(self._cells[i][j-1])
                result_of_inner = self._solve_r(i, j-1)
                if result_of_inner:
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i][j-1], True)
        
        if i < self.num_rows-1:
            if not self._cells[i+1][j].has_top_wall and not self._cells[i+1][j].visited:
                self._cells[i][j].draw_move(self._cells[i+1][j])
                result_of_inner = self._solve_r(i+1, j)
                if result_of_inner:
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i+1][j], True)

        if i > 0:
            if not self._cells[i-1][j].has_bottom_wall and not self._cells[i-1][j].visited:
                self._cells[i][j].draw_move(self._cells[i-1][j])
                result_of_inner = self._solve_r(i-1, j)
                if result_of_inner:
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i-1][j], True)
       
        return False

    def _create_cells(self):
        self._cells = []
        for i in range(self.num_rows):
            self._cells.append([Cell(self.__win) for j in range(self.num_cols)])
        i = 0
        if not self.test:
            for _ in self._cells:
                j = 0
                for _ in self._cells[i]:
                    self._draw_cell(i,j)
                    j += 1
                i += 1

    def _draw_cell(self, i, j):
        top_left = Point((self.x1 + (j* self.cell_size_x)),
                          (self.y1 + (i * self.cell_size_y)))
        
        bottom_right = Point((self.x1 + (j* self.cell_size_x) + self.cell_size_x),
                          (self.y1 + (i * self.cell_size_y) + self.cell_size_y))
        
        self._cells[i][j].draw(top_left, bottom_right)

        self._animate()

    def _animate(self):
        self.__win.redraw()
        time.sleep(0.01)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[self.num_rows-1][self.num_cols-1].has_bottom_wall = False
        if not self.test:
            self._draw_cell(0,0)
            self._draw_cell(self.num_rows-1, self.num_cols-1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        
        while True:
            to_visit = []

            # check for cells directly adjacent if visited rem[row][column]
            if i < self.num_rows-1:
                if [i+1, j] not in to_visit and not self._cells[i+1][j].visited:
                    to_visit.append([i+1, j])
                
            if i > 0:
                if [i-1, j] not in to_visit and not self._cells[i-1][j].visited:
                    to_visit.append([i-1, j])
            
            if j < self.num_cols-1:
                if [i, j+1] not in to_visit and not self._cells[i][j+1].visited:
                    to_visit.append([i, j+1])
            
            if j > 0:
                if [i, j-1] not in to_visit and not self._cells[i][j-1].visited:
                    to_visit.append([i, j-1])

            
            
            
            #check if further direction
            if len(to_visit) == 0:
                if not self.test:
                    self._draw_cell(i,j)
                return
            
            # identify next cell to enter
            next_cell_index = random.choice(to_visit)

            # break wall between current and chosen cell
            if i < next_cell_index[0]:
                self._cells[i][j].has_bottom_wall = False
                self._cells[next_cell_index[0]][next_cell_index[1]].has_top_wall = False
                if not self.test:
                    self._draw_cell(i, j)
                    self._draw_cell(next_cell_index[0], next_cell_index[1])

            elif j < next_cell_index[1]:
                self._cells[i][j].has_right_wall = False
                self._cells[next_cell_index[0]][next_cell_index[1]].has_left_wall = False
                if not self.test:
                    self._draw_cell(i, j)
                    self._draw_cell(next_cell_index[0], next_cell_index[1])
            
            elif i > next_cell_index[0]:
                self._cells[i][j].has_top_wall = False
                self._cells[next_cell_index[0]][next_cell_index[1]].has_bottom_wall = False
                if not self.test:
                    self._draw_cell(i, j)
                    self._draw_cell(next_cell_index[0], next_cell_index[1])
            
            elif j > next_cell_index[1]:
                self._cells[i][j].has_left_wall = False
                self._cells[next_cell_index[0]][next_cell_index[1]].has_right_wall = False
                if not self.test:
                    self._draw_cell(i, j)
                    self._draw_cell(next_cell_index[0], next_cell_index[1])

            #move to chosen cell recursively
            self._break_walls_r(next_cell_index[0], next_cell_index[1])

    def _reset_cells_visited(self):
        for i in self._cells:
            for j in i:
                j.visited = False


