import tkinter as tk

# Define a Point class
class Point:
    def __init__(self, x, y, color="black"):
        self.x = x
        self.y = y
        self.color = color

# Define a Rectangle class
class Rectangle:
    def __init__(self, x1, y1, x2, y2, color="blue"):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color

# Define a Circle class
class Circle:
    def __init__(self, center, radius, color="red"):
        self.center = center  # a Point
        self.radius = radius
        self.color = color

# a & b. Draw a rectangle using its color attribute
def draw_rectangle(canvas, rectangle):
    canvas.create_rectangle(
        rectangle.x1, rectangle.y1,
        rectangle.x2, rectangle.y2,
        fill=rectangle.color
    )

# c. Draw a point (as a small circle to make it visible)
def draw_point(canvas, point):
    r = 2  # small radius for visibility
    canvas.create_oval(
        point.x - r, point.y - r,
        point.x + r, point.y + r,
        fill=point.color
    )

# d. Draw a circle
def draw_circle(canvas, circle):
    x = circle.center.x
    y = circle.center.y
    r = circle.radius
    canvas.create_oval(
        x - r, y - r,
        x + r, y + r,
        fill=circle.color
    )

# GUI setup
root = tk.Tk()
root.title("Shapes Drawing")

canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# Create and draw a rectangle
rect = Rectangle(50, 50, 200, 150, color="green")
draw_rectangle(canvas, rect)

# Create and draw a point
pt = Point(100, 100, color="black")
draw_point(canvas, pt)

# Create and draw circles
circle1 = Circle(Point(300, 100), 40, color="red")
circle2 = Circle(Point(150, 250), 30, color="purple")
draw_circle(canvas, circle1)
draw_circle(canvas, circle2)

root.mainloop()
