import turtle as t
import random

turtle = t.Turtle()
turtle.speed("fastest")
t.colormode(255) # Set the color mode to 255 for RGB tuples

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        turtle.color(random_color()) # Uses your color list!
        turtle.circle(100)
        turtle.setheading(turtle.heading() + size_of_gap)  # Rotate the turtle by the specified gap for the next circle

draw_spirograph(5)  # You can change the gap size to see different effects
screen = t.Screen()
screen.exitonclick()