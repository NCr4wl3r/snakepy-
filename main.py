from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("PySnake game!")
screen.tracer(0)

snake = Snake()


game_is_on = True


counter = 0

while game_is_on:
    screen.update()
    counter += 1
    snake.move_snake()
    time.sleep(0.5)


screen.exitonclick()
