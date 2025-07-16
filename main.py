from window import Window, Point, Line
from cell import Cell
from maze import Maze


def main():
    """
    Initializes and runs the maze generation and solving application.
    Sets up window dimensions, maze parameters, and starts the event loop.
    """
    # Define window dimensions
    window_width = 800
    window_height = 600
    
    # Initialize the main drawing window
    # Added 100 to height to accommodate the "Solve Maze" button at the bottom
    window = Window(window_width, window_height + 100) 

    # Define margins for the maze within the window
    maze_margin_x = 50
    maze_margin_y = 50
    
    # Define the number of rows and columns for the maze grid
    num_rows = 10
    num_cols = 20
    
    # Calculate individual cell dimensions based on total maze area and cell count
    cell_width = (window_width - (2 * maze_margin_x)) / num_cols
    cell_height = (window_height - (2 * maze_margin_y)) / num_rows
    
    # Create the Maze instance, passing all necessary parameters
    # The maze generation and drawing happens within the Maze.__init__
    maze = Maze(
        maze_margin_x, maze_margin_y,
        num_rows, num_cols,
        cell_width, cell_height,
        window # Pass the window instance for drawing
    )

    # Start the window's event loop; waits until the window is closed by the user
    window.wait_for_close()

# Entry point for the script execution
if __name__ == "__main__":
    main()