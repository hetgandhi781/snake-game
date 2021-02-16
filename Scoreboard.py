from turtle import Turtle

FONT = ("Courier", 20, "normal")
ALIGNMENT = "center"


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 270)
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def update_score(self):
        self.write(f"score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

