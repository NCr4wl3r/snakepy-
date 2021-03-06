from turtle import Turtle

MOVE_DISTANCE = 20
LEFT = 180
UP = 90
RIGHT = 0
DOWN = 270


class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.create_snake()

    def create_body_square(self, position):
        snake_body = Turtle(shape="square")
        snake_body.color("white")
        snake_body.penup()
        snake_body.goto(position)
        return snake_body

    def create_snake(self):
        for ind in range(3):
            segment = self.create_body_square((-20 * ind, 0))
            self.segments.append(segment)
        self.head = self.segments[0]

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()

    def extend(self):
        segment = self.create_body_square(self.segments[-1].position())
        self.segments.append(segment)

    def move(self):
        for index in range(len(self.segments) - 1, 0, -1):
            # move every section to occupy the place of the next one
            new_position = self.segments[index - 1].pos()
            self.segments[index].goto(new_position)

        # move the head fo the snake 20 pixels to move forward
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
