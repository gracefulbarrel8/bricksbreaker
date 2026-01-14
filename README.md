# 🧱 Python Brick Breaker

This is a classic Brick Breaker game I built for my Grade 11 Computer Science project using **Python** and the **Turtle** library. 

---

## 🎮 How to Play
* **Goal:** Break all the blocks by bouncing the ball off your paddle.
* **Controls:** Press and hold the **Left** and **Right** arrow keys to move the paddle smoothly.
* **Lives:** Don't let the ball hit the floor, or you will lose a life!

## ✨ Key Features
* **Smooth Paddle Movement:** I optimized the controls using a dictionary to track key presses, removing the "stutter" effect.
* **Scoreboard:** Real-time score tracking as you destroy blocks.
* **Lives System:** Players have a limited number of lives before the game ends.
* **Object-Oriented Programming (OOP):** The game is organized into separate classes for the Ball, Paddle, Blocks, and Scoreboard.

## 🛠️ Technical Details
One of the biggest challenges was making the paddle move smoothly. I solved this by using `onkeypress` and `onkeyrelease` together to tell the game exactly when I am holding a key down. This makes the gameplay feel much more responsive.

## 📂 Project Structure
* **main.py**: The central engine that runs the game loop and collision logic.
* **paddle.py**: Handles the paddle's movement and screen boundaries.
* **ball.py**: Manages the physics and bouncing logic of the ball.
* **block.py**: Generates the grid of bricks.
* **scoreboard.py & lives.py**: Handles the game data and UI.

---
*Created by Aarav - Grade 11 CS Project*
