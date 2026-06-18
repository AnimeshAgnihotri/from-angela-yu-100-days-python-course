import random
from turtle import Turtle
from turtle import Screen
timmy=Turtle()
timmy.shape("circle")
timmy.color("red")
for i in range(4):
    timmy.forward(100)
    timmy.left(90)
listt=[]
for i in range(0,100, 2):
    listt.append(i)
for i in range(10): #draws square then golden ratio
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()
    timmy.forward(10)
    timmy.left(listt[i])


    #timmy.right(listt[i])
a=[]
for i in range(3, 50, 1):
    if 360%i==0:
        a.append(i)
print(a)
colors=["red", "green", "blue", "black", "yellow", "violet", "brown"]


for i in a:
    print(i)
    k=0
    while k in range(i):
        timmy.color(random.choice(colors))
        timmy.forward(35)
        timmy.left(360/i)
        print(360/i)
        k=k+1


screen = Screen()
screen.exitonclick()