from turtle import Screen
from snake import Snake
from food import Food
from scorebord import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreborad = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.left, "a")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")


game = True
while game:
    screen.update()
    time.sleep(.1)
    snake.move()

    # Food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreborad.increase_score()

    # Wall
    if snake.head.xcor() > 380 or snake.head.xcor() < -380 or snake.head.ycor() > 360 or snake.head.ycor() < -380:
        scoreborad.reset_score()
        snake.reset()

    # Hit itself
    for seg in snake.seg[1:]:
        if snake.head.distance(seg) < 10:
            scoreborad.reset_score()
            snake.reset()

screen.exitonclick()
