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
        self.high_score = self.read_file_data()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.string = f"Score:  {self.score} High score : {self.high_score}"
        self.write(self.string, align=ALIGMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.high_score < self.score:
            self.high_score = self.score
            self.save_file_data()
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto((-5, 0))
        self.write("GAME OVER", align=ALIGMENT, font=FONT)

    def read_file_data(self):
        with open("data.txt") as file:
            return int(file.read())

    def save_file_data(self):
        with open("data.txt", mode="w") as file:
            file.write(str(self.high_score))
