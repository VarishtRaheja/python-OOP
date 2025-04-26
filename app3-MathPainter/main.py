# Importing site packages
import numpy as np
from PIL import Image

# Crating the classes for the canvas and shapes.
class Canvas():
    """ Creating the constructor to input width,height and color of the drawing area(canvas). """
    def __init__(self, width, height, color):
        """ Creating a matrix of zeroes of the height and width. """
        self.width = width
        self.height = height
        self.color = color

        # Creating a 3d array for canvas creation
        self.data = np.zeros((self.height, self.width, len(self.color)), dtype=np.uint8)
        # Change color according to user input
        self.data[:] = self.color

    def make(self, imagepath, channel):
        """ Saving the image in the directory. """
        img = Image.fromarray(self.data, channel)
        return img.save(imagepath)

class Square:
    """ Drawing the square object. """
    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color


    def draw(self, canvas):
        canvas.data[self.x:self.x + self.side, self.y:self.y + self.side] = self.color


class Rectangle():
    """ Drawing the rectangle object. """
    def __init__(self, x, y, height, width, color):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.color = color

    def draw(self, canvas):
        canvas.data[self.x:self.x + self.height, self.y:self.y + self.width] = self.color


# Create the user defined functions
canvas_width = int(input("Enter the canvas width: "))
canvas_height = int(input("Enter the canvas height: "))
canvas_color = list(map(int, input("Enter the RGB values (0-255): ").split(",", 3)))


# Create the class objects and call the methods
def main():
    """ Calling all methods in a main function."""
    canvas = Canvas(canvas_width, canvas_height, canvas_color)
    r1 = Rectangle(x=3, y=4, height=20, width=50, color=(0, 0, 0))
    r1.draw(canvas)
    s1 = Square(x=(r1.x+r1.height),y=(r1.y+r1.width),side=50,color=(255,0,0))
    s1.draw(canvas)
    canvas.make(imagepath="canvas_test.png", channel="RGB")


if __name__ == "__main__":
    main()
