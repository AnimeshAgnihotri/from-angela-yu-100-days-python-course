from threading import TIMEOUT_MAX
from turtle import Turtle, Screen
timmy=Turtle()
my_screen = Screen()
timmy.color("red")
timmy.shape("turtle")
def move_forward():
    timmy.forward(10)
my_screen.listen()
def move_backward():
    timmy.backward(10)
def move_left():
    timmy.left(10)
    timmy.forward(10)
def move_right():
    timmy.right(10)
    timmy.forward(10)
def turn_north():
    timmy.setheading(90)
def turn_south():
    timmy.setheading(270)
def turn_east():
    timmy.setheading(0)
def turn_west():
    timmy.setheading(180)
def clearS():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()
my_screen.onkey(key="w", fun= move_forward) #when function used in side function then we dont need ()
my_screen.onkey(key="s", fun= move_backward)
my_screen.onkey(key="a", fun= move_left)
my_screen.onkey(key="d", fun=move_right)
my_screen.onkey(key="Up", fun= turn_north)
my_screen.onkey(key="Down", fun=turn_south)
my_screen.onkey(key="Left", fun= turn_west)
my_screen.onkey(key="Right", fun=turn_east)
my_screen.onkey(key="c", fun=clearS)
my_screen.exitonclick()