from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.color("white")

    def add_score_l(self):
        self.clear()
        self.goto(-100, 270)
        self.write(self.l_score, align="center", font=("Arial", 34, "bold"))
        self.l_score += 1

    def add_score_r(self):
        self.clear()
        self.goto(100, 270)
        self.write(self.r_score, align="center", font=("Arial", 34, "bold"))
        self.r_score += 1
