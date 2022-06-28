from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("PySnake game!")

snake = []


def create_body_square(pos_x, pos_y):
    snake_body = Turtle(shape="square")
    snake_body.color("white")
    snake_body.penup()
    snake_body.goto(x=pos_x, y=pos_y)
    return snake_body


# create snake
for ind in range(3):
    snake_body = create_body_square(pos_x=-20 * ind, pos_y=0)
    snake.append(snake_body)


screen.exitonclick()
