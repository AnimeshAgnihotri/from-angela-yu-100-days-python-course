from turtle import  Screen
import time
import snake, food, score

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake Game")
screen.setup(width=600, height=600)

snake=snake.SnakeClass()
food =food.Food()
snake_score=score.Score()
game=True
count=0
while game:
    screen.update()
    time.sleep(0.1)
    snake.movement()
    if snake.snake_list[0].distance(food)<20:# detect collision with food
        snake_score.counting()
        food.refresh_location()
        snake.extend_snake()

#detect collision with wall
    if snake.snake_list[0].xcor()>280 or snake.snake_list[0].xcor()<-280 or snake.snake_list[0].ycor()>280 or snake.snake_list[0].ycor()<-280:
        game=False
        snake_score.game_over()
#detect collision with tail
    for i in snake.snake_list[1:]:
        # if i ==snake.snake_list[0]:
        #     continue
        if snake.snake_list[0].distance(i)<10:
            game=False
            snake_score.game_over()
# print(f"score: {count} ")
screen.exitonclick()
