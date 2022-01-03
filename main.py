from turtle import Screen
from snake import Snake
from food import Food
from score_board import Score
import time

screen = Screen()
screen.title("Snake Game")
screen.bgcolor('deep sky blue')
screen.setup(width=620, height=600)
screen.tracer(0)

snake = Snake()
food = Food()
score_board = Score()

screen.listen()
screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Left', fun=snake.left)
screen.onkey(key='Right', fun=snake.right)

is_on = True
while is_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_length()

    if snake.head.distance(food) < 15:
        food.refresh_food()
        snake.grow_snake()
        score_board.refresh_score()

    x_wall = snake.head.xcor()
    y_wall = snake.head.ycor()
    if x_wall > 280 or x_wall < -300 or y_wall > 280 or y_wall < -280:
        score_board.reset()
        snake.reset()

    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            score_board.reset()
            snake.reset()


screen.exitonclick()
