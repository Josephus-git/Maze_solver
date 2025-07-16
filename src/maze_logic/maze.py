from maze_logic.cell import Cell
from gui.window import Point
import time
import random
from tkinter import Button

class Maze:
    """
    Represents a maze grid, handling its creation, wall breaking,
    and solving using a recursive backtracking algorithm.
    """
    def __init__(
            self, x_start, y_start,
            num_rows, num_cols,
            cell_width, cell_height,
            window_instance=None, is_test_mode=False,
            random_seed=None
    ):
        """
        Initializes a Maze object.

        Args:
            x_start (int): The starting X-coordinate (top-left) for drawing the maze.
            y_start (int): The starting Y-coordinate (top-left) for drawing the maze.
            num_rows (int): The number of rows in the maze grid.
            num_cols (int): The number of columns in the maze grid.
            cell_width (int): The width of each individual cell.
            cell_height (int): The height of each individual cell.
            window_instance (Window, optional): The window object to draw the maze on. Defaults to None.
            is_test_mode (bool): If True, disables drawing animations for faster testing. Defaults to False.
            random_seed (int, optional): Seed for the random number generator for reproducible maze generation.
        """
        # Store maze dimensions and drawing parameters
        self._x_start = x_start
        self._y_start = y_start
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_width = cell_width
        self._cell_height = cell_height
        
        # Store window instance and test mode flag
        self.__window = window_instance # Private: Direct interaction with the drawing window
        self._is_test_mode = is_test_mode # Protected: Controls animation/drawing for testing

        # Set random seed if provided for reproducible maze generation
        if random_seed is not None:
            random.seed(random_seed)
            
        # Maze cell grid
        self._cells = [] 

        # Maze generation steps
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_recursive(0, 0)
        self._reset_cells_visited() # Reset visited status for maze solving
        
        # Draw the solve button if a window is present
        if self.__window:
            self._draw_solve_button()

    def _draw_solve_button(self):
        """
        Draws the "Solve Maze" button on the window.
        """
        # Calculate button position for centering
        button_width_estimate = 7 * 10 # Rough estimate based on character count
        button_x = (self.__window.width / 2) - (button_width_estimate / 2)
        button_y = self.__window.height - 100

        solve_button = Button(
            self.__window.root, 
            text="Solve Maze",
            width=7, height=2, 
            command=self._on_solve_button_click, # Use a dedicated callback method
            background="blue", 
            foreground="white"
        )
        solve_button.place(x=button_x, y=button_y)

    def _on_solve_button_click(self):
        """
        Callback method for the "Solve Maze" button click. Initiates maze solving.
        """
        self.solve_maze() # Call the public solve method

    def solve_maze(self):
        """
        Initiates the recursive maze solving process from the top-left cell (0,0).
        """
        return self._solve_maze_recursive(0, 0)
    
    def _solve_maze_recursive(self, row_idx, col_idx):
        """
        Recursively solves the maze using depth-first search.

        Args:
            row_idx (int): Current row index of the cell.
            col_idx (int): Current column index of the cell.

        Returns:
            bool: True if a path to the exit is found from this cell, False otherwise.
        """
        self._animate() # Animate the current step
        self._cells[row_idx][col_idx].visited = True # Mark current cell as visited

        # Base case: If the current cell is the exit, return True
        if row_idx == self._num_rows - 1 and col_idx == self._num_cols - 1:
            return True
        
        # Define possible moves: right, left, down, up (in preferred order)
        # Check right neighbor
        if col_idx < self._num_cols - 1:
            next_cell = self._cells[row_idx][col_idx + 1]
            if not next_cell.has_left_wall and not next_cell.visited:
                self._cells[row_idx][col_idx].draw_move(next_cell) # Draw forward move
                if self._solve_maze_recursive(row_idx, col_idx + 1):
                    return True # Path found through this direction
                else:
                    self._cells[row_idx][col_idx].draw_move(next_cell, undo=True) # Undo move
        
        # Check left neighbor
        if col_idx > 0:
            next_cell = self._cells[row_idx][col_idx - 1]
            if not next_cell.has_right_wall and not next_cell.visited:
                self._cells[row_idx][col_idx].draw_move(next_cell) # Draw forward move
                if self._solve_maze_recursive(row_idx, col_idx - 1):
                    return True # Path found through this direction
                else:
                    self._cells[row_idx][col_idx].draw_move(next_cell, undo=True) # Undo move
        
        # Check down neighbor
        if row_idx < self._num_rows - 1:
            next_cell = self._cells[row_idx + 1][col_idx]
            if not next_cell.has_top_wall and not next_cell.visited:
                self._cells[row_idx][col_idx].draw_move(next_cell) # Draw forward move
                if self._solve_maze_recursive(row_idx + 1, col_idx):
                    return True # Path found through this direction
                else:
                    self._cells[row_idx][col_idx].draw_move(next_cell, undo=True) # Undo move

        # Check up neighbor
        if row_idx > 0:
            next_cell = self._cells[row_idx - 1][col_idx]
            if not next_cell.has_bottom_wall and not next_cell.visited:
                self._cells[row_idx][col_idx].draw_move(next_cell) # Draw forward move
                if self._solve_maze_recursive(row_idx - 1, col_idx):
                    return True # Path found through this direction
                else:
                    self._cells[row_idx][col_idx].draw_move(next_cell, undo=True) # Undo move
       
        return False # No path found from this cell

    def _create_cells(self):
        """
        Initializes the 2D grid of Cell objects.
        Each cell is also drawn on the window if not in test mode.
        """
        self._cells = []
        for r in range(self._num_rows):
            row_of_cells = []
            for c in range(self._num_cols):
                cell = Cell(self.__window) # Pass window instance to each cell
                row_of_cells.append(cell)
            self._cells.append(row_of_cells)
        
        # Draw all cells initially if not in test mode
        if not self._is_test_mode:
            for r in range(self._num_rows):
                for c in range(self._num_cols):
                    self._draw_cell(r, c)

    def _draw_cell(self, row_idx, col_idx):
        """
        Calculates cell coordinates and draws a specific cell on the window.

        Args:
            row_idx (int): The row index of the cell to draw.
            col_idx (int): The column index of the cell to draw.
        """
        if self.__window is None:
            return # Do not draw if no window is available

        # Calculate top-left and bottom-right points for the current cell
        x1 = self._x_start + (col_idx * self._cell_width)
        y1 = self._y_start + (row_idx * self._cell_height)
        top_left_point = Point(x1, y1)
        
        x2 = x1 + self._cell_width
        y2 = y1 + self._cell_height
        bottom_right_point = Point(x2, y2)
        
        # Draw the cell using its draw method
        self._cells[row_idx][col_idx].draw(top_left_point, bottom_right_point)
        self._animate() # Animate after drawing each cell

    def _animate(self):
        """
        Redraws the window and pauses briefly to show animation.
        Only runs if a window is available and not in test mode.
        """
        if self.__window and not self._is_test_mode:
            self.__window.redraw()
            time.sleep(0.01)

    def _break_entrance_and_exit(self):
        """
        Removes the top wall of the starting cell and the bottom wall of the ending cell.
        """
        # Break top wall of the entrance cell (0, 0)
        self._cells[0][0].has_top_wall = False
        # Break bottom wall of the exit cell (last_row, last_col)
        self._cells[self._num_rows - 1][self._num_cols - 1].has_bottom_wall = False
        
        # Redraw these specific cells to reflect wall changes
        if not self._is_test_mode:
            self._draw_cell(0, 0)
            self._draw_cell(self._num_rows - 1, self._num_cols - 1)

    def _break_walls_recursive(self, row_idx, col_idx):
        """
        Recursively breaks walls to generate the maze using a depth-first search algorithm.

        Args:
            row_idx (int): The current row index of the cell.
            col_idx (int): The current column index of the cell.
        """
        self._cells[row_idx][col_idx].visited = True # Mark current cell as visited
        
        while True:
            unvisited_neighbors = [] # List to store coordinates of unvisited neighbors

            # Check all four neighbors (right, left, down, up)
            # Right neighbor
            if col_idx < self._num_cols - 1 and not self._cells[row_idx][col_idx + 1].visited:
                unvisited_neighbors.append((row_idx, col_idx + 1))
            
            # Left neighbor
            if col_idx > 0 and not self._cells[row_idx][col_idx - 1].visited:
                unvisited_neighbors.append((row_idx, col_idx - 1))
            
            # Down neighbor
            if row_idx < self._num_rows - 1 and not self._cells[row_idx + 1][col_idx].visited:
                unvisited_neighbors.append((row_idx + 1, col_idx))
            
            # Up neighbor
            if row_idx > 0 and not self._cells[row_idx - 1][col_idx].visited:
                unvisited_neighbors.append((row_idx - 1, col_idx))
            
            # If no unvisited neighbors, backtrack (all paths explored from this cell)
            if not unvisited_neighbors:
                if not self._is_test_mode:
                    self._draw_cell(row_idx, col_idx) # Redraw cell to update wall status
                return
            
            # Choose a random unvisited neighbor
            next_row, next_col = random.choice(unvisited_neighbors)

            # Break walls between the current cell and the chosen neighbor
            # Moving Right
            if next_col > col_idx: # Current cell's right wall and neighbor's left wall
                self._cells[row_idx][col_idx].has_right_wall = False
                self._cells[next_row][next_col].has_left_wall = False
            # Moving Left
            elif next_col < col_idx: # Current cell's left wall and neighbor's right wall
                self._cells[row_idx][col_idx].has_left_wall = False
                self._cells[next_row][next_col].has_right_wall = False
            # Moving Down
            elif next_row > row_idx: # Current cell's bottom wall and neighbor's top wall
                self._cells[row_idx][col_idx].has_bottom_wall = False
                self._cells[next_row][next_col].has_top_wall = False
            # Moving Up
            elif next_row < row_idx: # Current cell's top wall and neighbor's bottom wall
                self._cells[row_idx][col_idx].has_top_wall = False
                self._cells[next_row][next_col].has_bottom_wall = False

            # Redraw affected cells immediately if not in test mode
            if not self._is_test_mode:
                self._draw_cell(row_idx, col_idx)
                self._draw_cell(next_row, next_col)

            # Recursively call _break_walls_recursive for the chosen neighbor
            self._break_walls_recursive(next_row, next_col)

    def _reset_cells_visited(self):
        """
        Resets the 'visited' status of all cells to False.
        This is crucial before running the maze solving algorithm.
        """
        for row in self._cells:
            for cell in row:
                cell.visited = False