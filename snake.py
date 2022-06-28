from turtle import Turtle


class Snake:
    snake = []

    def __init__(self) -> None:
        for ind in range(3):
            self.segment = self.create_body_square(pos_x=-20 * ind, pos_y=0)
            self.snake.insert(0, self.segment)


    def create_body_square(self, pos_x, pos_y):
        snake_body = Turtle(shape="square")
        snake_body.color("white")
        snake_body.penup()
        snake_body.goto(x=pos_x, y=pos_y)
        return snake_body

    def move_snake(self):
        for index in range(len(self.snake)):
            # move every section to occupy the place of the next one
            if index < len(self.snake) - 1:
                new_position = self.snake[index + 1].pos()
                self.snake[index].goto(new_position)

            # move the head fo the snake 20 pixels to move forward
            else:
                self.snake[index].forward(20)
