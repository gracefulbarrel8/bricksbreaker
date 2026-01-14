from turtle import Turtle

class Lives(Turtle):
    def __init__(self):
        self.live = 4
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(230, 270)
        self.write(f"Lives: {self.live}", False, "center", ("Arial", 15, "normal"))

    def lose_a_live(self):
        self.clear()
        self.live -= 1
        self.write(f"Lives: {self.live}", False, "center", ("Arial", 15, "normal"))