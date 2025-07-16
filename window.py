from tkinter import Tk, BOTH, Canvas

class Window:
    """
    Manages the main application window for drawing the maze.
    Handles window creation, drawing, updates, and closing.
    """
    def __init__(self, width, height):
        """
        Initializes the application window.

        Args:
            width (int): The width of the window in pixels.
            height (int): The height of the window in pixels.
        """
        self._width = width  # Internal window width
        self._height = height # Internal window height
        
        self.root = Tk() # Main Tkinter window instance
        self.root.title("Maze Solver") # Set window title
        
        # Set protocol for handling window close button (X)
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        
        # Create a Canvas widget for drawing
        self._canvas = Canvas(self.root, bg="white", height=self._height, width=self._width)
        self._canvas.pack(fill=BOTH, expand=1) # Pack canvas to fill the window
        
        self.__running = False # Internal flag to control the main loop

    @property
    def width(self):
        """Returns the width of the window."""
        return self._width

    @property
    def height(self):
        """Returns the height of the window."""
        return self._height

    def redraw(self):
        """
        Forces the window to update and redraw its contents.
        Useful for animation.
        """
        self.root.update_idletasks() # Process pending events
        self.root.update()          # Update the window

    def wait_for_close(self):
        """
        Starts the main loop and keeps the window open until explicitly closed.
        """
        self.__running = True # Set running flag to True
        while self.__running:
            self.redraw() # Continuously redraw the window
        print("Window closed....") # Confirmation message

    def close(self):
        """
        Sets the internal flag to False, allowing the main loop to terminate
        and close the window.
        """
        self.__running = False

    def draw_line(self, line_object, fill_color="black"):
        """
        Draws a line on the canvas.

        Args:
            line_object (Line): The Line object containing the coordinates.
            fill_color (str): The color to draw the line. Defaults to "black".
        """
        line_object.draw(self._canvas, fill_color) # Delegate drawing to the Line object
            

class Point:
    """
    Represents a 2D coordinate point.
    """
    def __init__(self, x, y):
        """
        Initializes a Point object.

        Args:
            x (int): The X-coordinate.
            y (int): The Y-coordinate.
        """
        self.x = x # X-coordinate of the point
        self.y = y # Y-coordinate of the point


class Line:
    """
    Represents a line segment defined by two Point objects.
    """
    def __init__(self, point_1, point_2):
        """
        Initializes a Line object.

        Args:
            point_1 (Point): The starting point of the line.
            point_2 (Point): The ending point of the line.
        """
        self._x1 = point_1.x # X-coordinate of the first point
        self._y1 = point_1.y # Y-coordinate of the first point
        self._x2 = point_2.x # X-coordinate of the second point
        self._y2 = point_2.y # Y-coordinate of the second point


    def draw(self, canvas_instance, fill_color):
        """
        Draws the line on a given Tkinter Canvas.

        Args:
            canvas_instance (tkinter.Canvas): The Canvas object to draw on.
            fill_color (str): The color to draw the line.
        """
        canvas_instance.create_line(
            self._x1, self._y1, self._x2, self._y2, # Coordinates for the line
            fill=fill_color, # Line color
            width=2          # Line thickness
        )