from turtle import Turtle

ALIGMENT = "center"
FONT = ("Arial", 18, "normal")


class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.speed(0)
        self.hideturtle()
        self.color("white")
        self.goto((-5, 270))
        self.score = 0
        self.update_score()

    def update_score(self):
        self.string = f"Score:  {self.score}"
        self.write(self.string, align=ALIGMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto((-5, 0))
        self.write("GAME OVER", align=ALIGMENT, font=FONT)
