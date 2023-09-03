from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Initialize game objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Constants for wall collision
WALL_LIMIT = 280

# Listen to keyboard inputs
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Main game loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if abs(snake.head.xcor()) > WALL_LIMIT or abs(snake.head.ycor()) > WALL_LIMIT:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:  # Skip the head
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

# Exit the game when the screen is clicked
screen.exitonclick()
