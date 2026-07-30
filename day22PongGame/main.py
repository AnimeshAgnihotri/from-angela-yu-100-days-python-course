from turtle import Screen

import scoreboard
from ball import Ball
from paddle import Paddle
from time import sleep
from scoreboard import Scoreboard

from scoreboard import Scoreboard

my_screen = Screen()
#paddle = Turtle()
my_screen.tracer(0)

my_screen.bgcolor("black")
my_screen.title("pong game")
my_screen.setup(width=800, height=600)

r_paddle=Paddle((370,0))
l_paddle=Paddle((-370,0))
ball=Ball()

game_on=True
def change_state(key):
    game_on=False
my_screen.listen()
my_screen.onkey(fun=r_paddle.go_up, key="Up")
my_screen.onkey(fun=r_paddle.go_down, key="Down")
my_screen.onkey(fun=l_paddle.go_up, key="w")
my_screen.onkey(fun=l_paddle.go_down, key="s")
#my_screen.onkey(fun=change_state, key="Right")

scoreboard_l = Scoreboard()
scoreboard_r = Scoreboard()
scoreboard_r.add_score_r()
scoreboard_l.add_score_l()

while game_on:
    sleep(ball.move_speed)
    my_screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 60 and ball.xcor()>350:
        ball.bounce_x()
        ball.move_speed-=0.01
    if ball.distance(l_paddle) < 60 and ball.xcor()<-350:
        ball.bounce_x()
        ball.move_speed -=0.01
    if ball.xcor()>380:
        ball.reset()
        ball.move_speed = 0.1
        scoreboard_r.add_score_r()
    if ball.xcor()<-380:
        ball.reset()
        ball.move_speed=0.1
        scoreboard_l.add_score_l()
    if scoreboard_l.l_score>5 or scoreboard_r.r_score>5:
        game_on=False
        #my_screen.onkey(fun=ball.move, key="k")
my_screen.exitonclick()

