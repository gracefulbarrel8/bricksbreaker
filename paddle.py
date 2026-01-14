from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(1, 5)
        self.penup()
        self.goto(0, -270)

    def move_right(self):
        # Increased speed slightly for a more responsive feel
        new_x = self.xcor() + 15 
        if new_x < 250:  # Optional: Keep paddle within screen bounds
            self.goto(new_x, self.ycor())

    def move_left(self):
        new_x = self.xcor() - 15
        if new_x > -250: # Optional: Keep paddle within screen bounds
            self.goto(new_x, self.ycor())