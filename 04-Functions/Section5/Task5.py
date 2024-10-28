###
# Draws each of the figures (square, triangle, rectangle) twice,
# in different locations
#
import math
import turtle as t

# Set up the screen
window = t.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = t.Turtle()
pen.speed(5)   

## Draw figures
def DrawSquare(size):
    pen.pendown()
    for i in range(4):
        pen.forward(size)
        pen.right(90)
    
def DrawTriangle(size):
    pen.pendown()
    for i in range(3):
        pen.forward(size)
        pen.right(120)

def DrawRectangle(width, length):
    pen.pendown()
    pen.forward(width)
    pen.right(90)
    pen.forward(length)
    pen.right(90)
    pen.forward(width)
    pen.right(90)
    pen.forward(length)
    pen.right(90)

DrawSquare(30)
DrawRectangle(50,60)
DrawTriangle(70)

# Hide the turtle and finish
pen.hideturtle()
window.mainloop()