import turtle

my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
for _ in range(4):
    my_turtle.forward(100)
    my_turtle.left(90) 

screen = turtle.Screen()
screen.exitonclick()