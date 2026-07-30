
from turtle import Screen
from turtle_crossing import TurtleCrossing
from traffic import Traffic
my_screen = Screen()
my_screen.setup(width=800, height=600)
my_screen.bgcolor("white")
my_screen.title("Turtle Crossing")




turtle_crossing= TurtleCrossing()
turtle_crossing.enable_control()
traffic = Traffic()
traffic.create_car()


my_screen.exitonclick()
game_on=True
while game_on:
    for i in range(6):

            traffic.move_cars()

    traffic.create_car()
