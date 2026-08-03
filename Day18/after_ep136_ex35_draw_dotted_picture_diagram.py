import turtle
import random

# Setup
t = turtle.Turtle()
t.speed(0)  # Fastest speed
turtle.colormode(255)

# Define grid parameters
rows = 10
cols = 10
gap = 50  # Distance between dots
start_x = -((cols - 1) * gap) / 2
start_y = -((rows - 1) * gap) / 2

# Create a list of random colors or use predefined ones
colors = [(245, 243, 238), (246, 242, 244), (202, 164, 110), 
(240, 245, 241), (236, 239, 243), (149, 75, 50), 
(222, 201, 136), (53, 93, 123), (170, 154, 41), 
(138, 31, 20), (134, 163, 184), (197, 92, 73), 
(47, 121, 86), (73, 43, 35), (145, 178, 149), 
(14, 98, 70), (232, 176, 165), (160, 142, 158), 
(54, 45, 50), (101, 75, 77), (183, 205, 171), 
(36, 60, 74), (19, 86, 89), (82, 148, 129), 
(147, 17, 19), (27, 68, 102), (12, 70, 64), 
(107, 127, 153), (176, 192, 208), (168, 99, 102), 
(66, 64, 60), (219, 178, 183), (178, 198, 202), 
(112, 139, 141), (254, 194, 0)]

# Draw the 10x10 grid
for y in range(rows):
    for x in range(cols):
        # Move to the correct position
        t.penup()
        t.goto(start_x + x * gap, start_y + y * gap)
        t.pendown()
        
        # Draw a dot with a random color from the palette
        dot_color = random.choice(colors)
        t.dot(20, dot_color)

# Hide turtle and keep window open
t.hideturtle()
turtle.done()