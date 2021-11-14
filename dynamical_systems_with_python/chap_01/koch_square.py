"""
Name:           koch_square.py
Description:    A program for plotting a Koch square curve
"""

from turtle import *
import turtle

setpos(0, -250)                 # Set initial point.

def kock_square(length, level):
    speed(0)
    for i in range(4):
        plot_side(length, level)
        rt(90)
    turtle.getscreen().getcanvas().postscript(file='kock_square.ps')

def plot_side(length, level):
    if level == 0:
        fd(length)
        return
    plot_side(length/3, level-1)
    lt(90)
    plot_side(length/3, level-1)
    rt(90)
    plot_side(length/3, level-1)
    rt(90)
    plot_side(length/3, level-1)
    lt(90)
    plot_side(length/3, level-1)


if __name__ == "__main__":
    kock_square(200, 4)