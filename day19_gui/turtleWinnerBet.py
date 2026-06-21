from turtle import Turtle, Screen
import random
my_screen = Screen()
my_screen.setup(width=500, height=400)

turtle_color=["red", "green", "blue", "indigo", "yellow"]
turtle_instances=[]
game_going=False
user_bet=my_screen.textinput(  "turtle race", f"which turtle player you bet on player {turtle_color}")
if user_bet:
    game_going=True

for i in range (5): #defining 5 turtles each at every 40 distance in y cordinate
    timmy=Turtle()
    timmy.shape("turtle")
    timmy.color(turtle_color[i])
    timmy.penup()
    timmy.goto(-240, 60-i*40)
    timmy.pendown()
    turtle_instances.append(timmy)
while game_going:  #keeps runnning till first one hit xcor at 240, 240 bcz at 250 it cuts the turtle head since we defined the dimension as such

    for i in turtle_instances:
        i.pendown()
        i.forward(random.randint(0,20))
        if i.xcor() > 220:
            game_going=False
            if user_bet==i.color:
                print(f"{i.pencolor()} is the winner, you won")
            else:
                print(f"{i.pencolor()} is the winner, you lost")

# timmy = Turtle()
# timmy.penup()
# timmy.goto(-240, 100)
# timmy.shape("turtle")
# timmy.color("red")
# timmy.pendown()
# turtle_color.append("red")
#
# tommy=Turtle()
# tommy.penup()
# tommy.goto(-240, 60)
# tommy.shape("turtle")
# tommy.color("blue")
# tommy.pendown()
# turtle_color.append("blue")
#
# titty=Turtle()
# titty.penup()
# titty.goto(-240, 20)
# titty.shape("turtle")
# titty.color("green")
# titty.pendown()
# turtle_color.append("green")
#
# tutture=Turtle()
# tutture.penup()
# tutture.goto(-240,-20)
# tutture.shape("turtle")
# tutture.color("yellow")
# tutture.pendown()
# turtle_color.append("yellow")
#
# turture=Turtle()
# turture.penup()
# turture.goto(-240, -60)
# turture.shape("turtle")
# turture.color("indigo")
# turture.pendown()
# turtle_color.append("indigo")




#user_bet=my_screen.textinput(  "turtle race", f"which turtle player you bet on player {turtle_color}")
my_screen.exitonclick()
