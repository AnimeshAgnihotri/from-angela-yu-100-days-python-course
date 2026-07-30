from turtle import Turtle, Screen
import random

screen = Screen()

class SnakeClass:
    def __init__(self):
        self.snake_list = []
        self.position_xy = [(0, 0), (-20, 0), (-40, 0)]
        self.colors=["red", "green", "blue", "yellow", "cyan", "magenta", "orange", "purple"]
        self.snake_shapes=["arrow","circle","square", "turtle"]
        self.create_snake()

    def create_snake(self):
        for i in self.position_xy:
            self.snake_body(i)


    def snake_body(self,i):
        timmy = Turtle()
        timmy.shape(random.choice(self.snake_shapes))
        timmy.color(random.choice(self.colors))
        timmy.penup()
        timmy.goto(i)
        self.snake_list.append(timmy)

    def extend_snake(self):
        self.snake_body(self.snake_list[-1].position())


    def movement(self):
        for i in range(len(self.snake_list) - 1, 0, -1):
            x = self.snake_list[i - 1].xcor()
            y = self.snake_list[i - 1].ycor()
            self.snake_list[i].goto(x, y)
        self.direction_change()
        self.snake_list[0].forward(20)
        #self.snake_list[0].right(90)

    def direction_change(self):
        screen.listen()
        screen.onkey(key="Up",fun=self.move_up)
        screen.onkey(key="Down",fun= self.move_down)
        screen.onkey(key="Left", fun=self.move_left)
        screen.onkey(key="Right", fun=self.move_right)

    def move_up(self):
        if self.snake_list[0].heading()!=270:
            self.snake_list[0].setheading(90)

    def move_left(self):
        if self.snake_list[0].heading() != 0:
            self.snake_list[0].setheading(180)

    def move_right(self):
        if self.snake_list[0].heading() != 180:
            self.snake_list[0].setheading(0)

    def move_down(self):
        if self.snake_list[0].heading() != 90:
            self.snake_list[0].setheading(270)

#snake = SnakeClass()

