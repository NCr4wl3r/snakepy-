from turtle import Turtle

MOVE_DISTANCE = 20


class Snake:
    def __init__(self) -> None:
        self.snake = []
        for ind in range(3):
            self.segment = self.create_body_square(pos_x=-20 * ind, pos_y=0)
            self.snake.append(self.segment)

    def create_body_square(self, pos_x, pos_y):
        snake_body = Turtle(shape="square")
        snake_body.color("white")
        snake_body.penup()
        snake_body.goto(x=pos_x, y=pos_y)
        return snake_body

    def move(self):
        for index in range(len(self.snake)-1, 0, -1):
            # move every section to occupy the place of the next one
            new_position = self.snake[index - 1].pos()
            self.snake[index].goto(new_position)

        # move the head fo the snake 20 pixels to move forward
        self.snake[0].forward(MOVE_DISTANCE)
