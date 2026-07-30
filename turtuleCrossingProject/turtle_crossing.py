from turtle import Turtle, Screen
my_screen = Screen()
class TurtleCrossing(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("turtle")
        self.color("red")
        self.speed(1)
        self.penup()
        self.setheading(90)
    def enable_control(self):
        my_screen.listen()
        my_screen.onkey(self.up, "Up")
        my_screen.onkey(self.down, "Down")
    def up(self):
        self.setheading(90)
        self.forward(5)
    def down(self):
        self.setheading(270)
        self.forward(5)



