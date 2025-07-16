from window import Point, Line

class Cell:
    """
    Represents a single cell in a grid, typically used for maze generation.
    Each cell can have four walls (left, right, top, bottom) and a visited state.
    """
    def __init__(self, window_instance=None, has_left_wall=True, has_right_wall=True,
                 has_top_wall=True, has_bottom_wall=True):
        """
        Initializes a Cell object.

        Args:
            window_instance (Window, optional): The window object to draw on. Defaults to None.
            has_left_wall (bool): True if the cell has a left wall, False otherwise.
            has_right_wall (bool): True if the cell has a right wall, False otherwise.
            has_top_wall (bool): True if the cell has a top wall, False otherwise.
            has_bottom_wall (bool): True if the cell has a bottom wall, False otherwise.
        """
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self.__window = window_instance  # Private attribute for the drawing window
        self.visited = False             # Tracks if the cell has been visited during maze generation

        # Initialize coordinates to None; they are set when draw() is called
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None

    def draw(self, top_left_point, bottom_right_point, fill_color="black"):
        """
        Draws the cell's walls on the associated window.

        Args:
            top_left_point (Point): The top-left corner coordinates of the cell.
            bottom_right_point (Point): The bottom-right corner coordinates of the cell.
            fill_color (str): The color of the walls. Defaults to "black".
        """
        # Store cell coordinates as protected attributes
        self._x1 = top_left_point.x
        self._y1 = top_left_point.y
        self._x2 = bottom_right_point.x
        self._y2 = bottom_right_point.y

        # Define lines for each wall
        bottom_line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2)) 
        left_line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        right_line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        top_line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))

        # Check if a window instance is available for drawing
        if self.__window is None:
            print("Warning: No window instance provided to draw the cell.")
            return

        # Draw left wall based on its existence
        self.__window.draw_line(left_line, fill_color if self.has_left_wall else "white")
        
        # Draw right wall based on its existence
        self.__window.draw_line(right_line, fill_color if self.has_right_wall else "white")
        
        # Draw top wall based on its existence
        self.__window.draw_line(top_line, fill_color if self.has_top_wall else "white")
        
        # Draw bottom wall based on its existence
        self.__window.draw_line(bottom_line, fill_color if self.has_bottom_wall else "white")

    def draw_move(self, target_cell, undo=False):
        """
        Draws a line representing a "move" from this cell to a target cell.

        Args:
            target_cell (Cell): The cell to draw the move to.
            undo (bool): If True, draws the move in "grey" (undoing a previous move).
                         If False, draws in "red".
        """
        # Calculate the midpoint of the current cell
        current_cell_mid_x = (self._x1 + self._x2) / 2
        current_cell_mid_y = (self._y1 + self._y2) / 2

        # Calculate the midpoint of the target cell
        target_cell_mid_x = (target_cell._x1 + target_cell._x2) / 2
        target_cell_mid_y = (target_cell._y1 + target_cell._y2) / 2
        
        # Create a line connecting the midpoints
        move_line = Line(Point(current_cell_mid_x, current_cell_mid_y),
                         Point(target_cell_mid_x, target_cell_mid_y))

        # Check if a window instance is available for drawing
        if self.__window is None:
            print("Warning: No window instance provided to draw the move.")
            return

        # Determine the color based on the undo flag
        line_color = "grey" if undo else "red"
        self.__window.draw_line(move_line, line_color)