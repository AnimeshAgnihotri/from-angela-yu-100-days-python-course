from turtle import Turtle
from random import choice, randint


class Traffic:
    def __init__(self):

        self.list_color=["red","green","blue", "yellow", "cyan","magenta"]


        self.init_car_position=[[380,0], [380, 40], [380, -40]]
        self.last_car_position=[[-380,0], [-380, 40], [-380, -40]]
        self.car_list=[]
    def create_car(self):
        for i in range(len(self.init_car_position)):

            car=Turtle()
            car.penup()
            car.goto(self.init_car_position[i][0],self.init_car_position[i][1])
            car.color(choice(self.list_color))

            car.setheading(180)


            car.move_speed = randint(1, 5)
            self.car_list.append(car)

    def move_cars(self):
        for car in self.car_list:
            car.forward(car.move_speed)