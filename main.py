from turtle import Screen
from lives import Lives
from paddle import Paddle
from ball import Ball
from block import Block
from scoreboard import Scoreboard
import time

# --- SCREEN SETUP ---
screen = Screen()
screen.title("Aarav's Breaker Game")
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)

# --- GAME OBJECTS ---
my_paddle = Paddle()
my_ball = Ball()
my_block = Block()
all_blocks = my_block.blocks
score = Scoreboard()
lives = Lives()

# --- SMOOTH MOVEMENT SYSTEM ---
# This dictionary tracks which keys are currently held down
keys_pressed = {}

def press_left():
    keys_pressed["Left"] = True

def release_left():
    keys_pressed["Left"] = False

def press_right():
    keys_pressed["Right"] = True

def release_right():
    keys_pressed["Right"] = False

# Listeners for both pressing and releasing keys
screen.listen()
screen.onkeypress(press_left, "Left")
screen.onkeyrelease(release_left, "Left")
screen.onkeypress(press_right, "Right")
screen.onkeyrelease(release_right, "Right")

# --- MAIN GAME LOOP ---
is_game_on = True

while is_game_on:
    try:
        # Smaller sleep time = smoother animation
        time.sleep(0.01)
        screen.update()
        
        # Check held keys and move paddle
        if keys_pressed.get("Left"):
            my_paddle.move_left()
        if keys_pressed.get("Right"):
            my_paddle.move_right()

        my_ball.move_ball()

        # Detect collision with side walls
        if my_ball.xcor() < -280 or my_ball.xcor() > 280:
            my_ball.side_wall_bounce()

        # Detect collision with upper wall
        if my_ball.ycor() > 280:
            my_ball.bounce_y()

        # Detect collision with paddle
        if my_ball.distance(my_paddle) < 50 and my_ball.ycor() < -250:
            my_ball.bounce_y()

        # Detect collision with blocks
        for block in all_blocks:
            if my_ball.distance(block) < 30:
                block.goto(1000, 1000)  # Move block off-screen
                my_ball.bounce_y()
                score.add_to_score()

        # Detect when ball goes past paddle
        if my_ball.ycor() < -290:
            lives.lose_a_live()
            my_ball.reset_ball()

        # Detect game over
        if lives.live == 0:
            is_game_on = False
            score.game_over()

    except Exception:
        # Prevents error codes when closing the window with the 'X'
        is_game_on = False

# Exit logic
try:
    screen.exitonclick()
except Exception:
    pass