from turtle import *
import colorsys

# Setup the turtle environment
bgcolor("black")
speed(0)
width(2)
hideturtle()

# Generate a color palette
n = 36  # Number of colors
hues = [colorsys.hsv_to_rgb(i/n, 1, 1) for i in range(n)]

# Draw the pattern
for i in range(360):
    color(hues[i % n])  # Cycle through the color palette
    forward(i * 2)
    right(59)  # Change the angle for a unique pattern
    circle(i % 30 + 10, 180)  # Semi-circle for added complexity

# Finish the drawing
done()