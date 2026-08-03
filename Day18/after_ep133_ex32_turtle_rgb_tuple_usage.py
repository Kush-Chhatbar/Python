import turtle as t
import random

turtle = t.Turtle()
turtle.speed(10)
turtle.pensize(10)
t.colormode(255) # Set the color mode to 255 for RGB tuples

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

directions = [0, 90, 180, 270]

for _ in range(200):  
    turtle.color(random_color()) # Uses your color list!
    turtle.setheading(random.choice(directions))
    turtle.forward(25)

screen = t.Screen()
screen.exitonclick()