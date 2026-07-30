import colorgram
import random
from turtle import colormode, Turtle, Screen
my_screen = Screen()
timmy = Turtle()
colors=colorgram.extract('images.jpeg',30)
print(type(colors))


#print(dir(colors))
list_of_color=[]
def color_choose():

    for color in colors:
        r=color.rgb.r
        g=color.rgb.g
        b=color.rgb.b
       # print(r,g,b)
        list_of_color.append((r,g,b))


my_screen.setup(300, 300)
colormode(255)
print(colors)
color_choose()
print(list_of_color)

for i in range(10):
    for j in range(10):
        timmy.pendown()
        timmy.color(random.choice(list_of_color))
        #print(random.choice(list_of_color))
        timmy.dot(12)
        timmy.penup()
        timmy.forward(30)


    timmy.backward(300)  # Go back to start
    timmy.left(90)
    timmy.forward(30)  # Move down one row
    timmy.right(90)
    timmy.pendown()

my_screen.exitonclick()
