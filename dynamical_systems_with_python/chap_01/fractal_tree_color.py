"""
Name:           fractal_tree_color.py
Description:    A program for plotting fractal trees.
"""

from turtle import *
import turtle

setheading(90)                  # The turtle points straight up.
penup()                         # Lift the pen.
setpos(0, -250)                 # Set initial point.
pendown()                       # Pen down.

def fractal_tree_color(lentgh, level):
    """
    Draws a fractal tree
    """
    pensize(lentgh/10)          # Thickness of lines
    if (lentgh < 20):
        pencolor("green")
    else:
        pencolor("brown")
    speed(0)
    if (level > 0):
        fd(lentgh)
        rt(30)
        fractal_tree_color(lentgh * 0.7, level - 1)
        lt(90)
        fractal_tree_color(lentgh * 0.5, level - 1)
        rt(60)
        penup()
        bk(lentgh)
        pendown()
    turtle.getscreen().getcanvas().postscript(file='fractal_tree_color.ps')

if __name__ == "__main__":
    fractal_tree_color(200, 10)
    
    
