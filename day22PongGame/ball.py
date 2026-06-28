from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.goto(0,0)
        self.x_step=10
        self.y_step=10
        self.move_speed=0.1
    def move(self):
        x=self.xcor()
        y=self.ycor()
        self.goto(x+self.x_step,y+self.y_step)


    def bounce_y(self):
        self.y_step=self.y_step*-1

    def bounce_x(self):
        self.x_step = self.x_step * -1
    def reset(self):
        self.goto(0,0)
        self.bounce_x()