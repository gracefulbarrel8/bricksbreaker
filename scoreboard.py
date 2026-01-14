from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-230, 270)
        self.write(f"Score: {self.score}", False, "center", ("Arial", 15, "normal"))

    def add_to_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", False, "center", ("Arial", 15, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", False, "center", ("Arial", 15, "normal"))