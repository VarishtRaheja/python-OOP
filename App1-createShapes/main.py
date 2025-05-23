from random import randint
import turtle

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x \
                and rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else:
            return False


class Rectangle:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x) * \
               (self.point2.y - self.point1.y)


# Rectangle class being parent inside child class
class DrawRectangle(Rectangle):
    def draw(self,canvas):
        canvas.penup()
        canvas.goto(25,75)
        canvas.pendown()
        canvas.forward(100)
        canvas.left(90)
        canvas.forward(200)
        canvas.left(90)
        canvas.forward(100)
        canvas.left(90)
        canvas.forward(200)
        canvas.left(90)
        turtle.done()

canvas_rectangle = DrawRectangle(Point(randint(0, 400), randint(0, 400)),Point(randint(10, 400), randint(10, 400)))
draw_area = turtle.Turtle()
canvas_rectangle.draw(canvas=draw_area)
print(canvas_rectangle.area())
# Create rectangle object
# rectangle = Rectangle(Point(randint(0, 9), randint(0, 9)),
#                       Point(randint(10, 19), randint(10, 19)))

# Print rectangle coordinates
# print("Rectangle Coordinates: ",
#       rectangle.point1.x, ",",
#       rectangle.point1.y, "and",
#       rectangle.point2.x, ",",
#       rectangle.point2.y)
#
# # Get point and area from user
# user_point = Point(float(input("Guess x: ")), float(input("Guess y: ")))
# user_area = float(input("Guess rectangle area: "))
#
# # Print out the game result
# print("Your point was inside rectangle: ", user_point.falls_in_rectangle(rectangle))
# print("Your area was off by: ", rectangle.area() - user_area)
# print("The rectangle area is: {0}".format(rectangle.area()))
