import random
from turtle import Turtle, Screen, colormode
#from many_angles import color_chooser
#many_angles wont work because in many angles outside the color_chooser function there is running files with output
#if importing then make sure that file only has everything inside function or class
colormode(255)
timmy = Turtle()
def color_choose():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return r,g,b
size_of_gap=int(input("Enter the size of gap"))

for i in range(int(360/size_of_gap)):
    timmy.color(color_choose())
    timmy.circle(45)
    timmy.setheading(timmy.heading()+size_of_gap)




my_screen = Screen()
my_screen.exitonclick()

