from turtle import Turtle
import random
class  Food(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.color("green")
        self.refresh_location()

    def refresh_location(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)


        print(f" x coordinate= {self.xcor()},y coordinate= {self.ycor()}")
