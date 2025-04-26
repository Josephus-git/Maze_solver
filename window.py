from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.root = Tk()
        self.root.title("Maze Solver")
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.__C = Canvas(self.root, bg="white", height=self.__height, width=self.__width)
        self.__C.pack(fill=BOTH, expand=1)
        self.__running = False
        self.public_width = width
        self.public_height = height

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()  

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed....")

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color="black"):
            line.draw(self.__C, fill_color)

    


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point_1, point_2):
        self.__x1 = point_1.x
        self.__y1 = point_1.y
        self.__x2 = point_2.x
        self.__y2 = point_2.y


    def draw(self, canvas, fill_color):
        canvas.create_line(
        self.__x1, self.__y1, self.__x2, self.__y2, fill=fill_color, width=2
        )


