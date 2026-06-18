import random
from turtle import Turtle, Screen
my_screen = Screen()
timmy= Turtle()
print(timmy)

colors = ["red", "green", "yellow", "blue", "magenta", "cyan"]
direction=[90, 45, 10,20 ,40 ,35, 50, 76, 89, 91, 180, 145, 5 , 6 ,7 , 8 , 9 , 11, 23, 33, 43, 53, 63, 65]
speed=[10, 2, 3, 5 ,8]
distance=[5,10,15, 17 ,14, 50, 25, 26, 28 , 32 ,18 , 21]
i=random.choice(direction)
y=random.choice(direction)


for x in range(100):

    timmy.shape("turtle")
    timmy.color(random.choice(colors))
    timmy.speed(random.choice(speed))
    timmy.forward( random.choice(distance))
    timmy.setheading(random.choice(direction))
    timmy.backward(random.choice(distance))
    timmy.setheading(random.choice(direction))
    timmy.forward(random.choice(distance))
    timmy.setheading(random.choice(direction))
    timmy.backward(random.choice(distance))
    timmy.width(x)



my_screen.exitonclick()
print(my_screen.canvheight)