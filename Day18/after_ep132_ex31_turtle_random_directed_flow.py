from turtle import Turtle, Screen
import random

turtle = Turtle()
turtle.speed(10)
turtle.pensize(10)

colors = [
    "crimson", 
    "deepskyblue", 
    "forestgreen", 
    "darkorange", 
    "mediumorchid", 
    "gold", 
    "hotpink", 
    "turquoise", 
    "violet", 
    "tomato"
]

directions = [0, 90, 180, 270]

for _ in range(200):  
    turtle.color(random.choice(colors)) # Uses your color list!
    turtle.setheading(random.choice(directions))
    turtle.forward(25)

screen = Screen()
screen.exitonclick()