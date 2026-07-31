from turtle import Turtle, Screen
import random

turtle = Turtle()

colors = [
    "crimson", 
    "deepskyblue", 
    "forestgreen", 
    "darkorange", 
    "mediumorchid", 
    "gold", 
    "hotpink", 
    "turquoise", 
    "slateviolet", 
    "tomato"
]

def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        turtle.forward(100)
        turtle.right(angle)

for shape_n in range(3, 11):
    turtle.pencolor(random.choice(colors))
    draw_shape(shape_n)

screen = Screen()
screen.exitonclick()