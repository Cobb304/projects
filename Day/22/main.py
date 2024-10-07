from paddle import Paddle
from turtle import Screen
from ball import Ball
from scoreboard import Scoreboard
import time
from os import system
system("cls")

my_screen = Screen()
my_screen.setup(800, 600)
my_screen.bgcolor("black")
my_screen.title("Pong")
my_screen.tracer(0)

r_paddle = Paddle(350)
l_paddle = Paddle(-350)
scoreboard = Scoreboard()
ball = Ball()

my_screen.listen()
my_screen.onkey(lambda: r_paddle.keybinds("Up"), "Up")
my_screen.onkey(lambda: r_paddle.keybinds("Down"), "Down")
my_screen.onkey(lambda: l_paddle.keybinds("w"), "w")
my_screen.onkey(lambda: l_paddle.keybinds("s"), "s")

game_on = True
start_pause = True
while game_on:
    time.sleep(0.03)
    my_screen.update()

    if start_pause:
        time.sleep(0.5)
        start_pause = False

    ball.ball_movement()

    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.wall_bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.paddle_bounce()

    if ball.xcor() > 420 or ball.xcor() < -420:
        scoreboard.plusOne(ball.xcor())
        ball.ball_out()
        start_pause = True










my_screen.exitonclick()