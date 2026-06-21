from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 270)
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()


    def counting(self):
        self.score+=1
        self.clear()
        self.write(f"Score{self.score}", move =False,align="center", font=("Courier", 24, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write("Game Over", move=False, align="center", font=("Courier", 24, "normal"))
