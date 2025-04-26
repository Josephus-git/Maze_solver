from window import Point, Line

class Cell:
    def __init__(self, win=None, left=True, right=True, top=True, bottom=True):
        self.has_left_wall = left
        self.has_right_wall = right
        self.has_top_wall = top
        self.has_bottom_wall = bottom
        self.__win = win
        self.visited = False

    def draw(self,top_left, bottom_right, fill_color="black"):
        self.__x1 = top_left.x
        self.__y1 = bottom_right.y
        self.__x2 = bottom_right.x
        self.__y2 = top_left.y
        
        bottom_line = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
        left_line = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
        right_line = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
        top_line = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))

        if self.has_left_wall:
             self.__win.draw_line(left_line, fill_color)
        else:
             self.__win.draw_line(left_line, "white")
        
        if self.has_right_wall:
             self.__win.draw_line(right_line, fill_color)
        else:
             self.__win.draw_line(right_line, "white")
        
        if self.has_top_wall:
             self.__win.draw_line(top_line, fill_color)
        else:
             self.__win.draw_line(top_line, "white")
        
        if self.has_bottom_wall:
             self.__win.draw_line(bottom_line, fill_color)
        else:
             self.__win.draw_line(bottom_line, "white")

    def draw_move(self, to_cell, undo=False):
          x_1 = (self.__x2 - self.__x1)/2 + self.__x1
          y_1 = (self.__y2 - self.__y1)/2 + self.__y1
          x_2 = (to_cell.__x2 - to_cell.__x1)/2 + to_cell.__x1
          y_2 = (to_cell.__y2 - to_cell.__y1)/2 + to_cell.__y1
          mid_line = Line(Point(x_1, y_1), Point(x_2, y_2))
          if not undo:
              self.__win.draw_line(mid_line, "red")
          else:
              self.__win.draw_line(mid_line, "grey")


 