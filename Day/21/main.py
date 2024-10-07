from snake import Snake
from food import Food
from scoreBoard import ScoreBoard
import time
from os import system
system("cls")

snake = Snake(3)
screen = snake.screen
food = Food()
scoreBoard = ScoreBoard()

screen.onkey(lambda: snake.turn("Up"), "Up")
screen.onkey(lambda: snake.turn("Right"), "Right")
screen.onkey(lambda: snake.turn("Down"), "Down")
screen.onkey(lambda: snake.turn("Left"), "Left")
screen.listen()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.15)
    snake.move()

    if snake.snake_blocks[0].distance(food) < 15:
        food.refresh()
        snake.add_block()
        scoreBoard.plusOne()
        print("+1")
    
    if snake.snake_blocks[0].xcor() > 280 or snake.snake_blocks[0].xcor() < -280 or snake.snake_blocks[0].ycor() > 280 or snake.snake_blocks[0].ycor() < -280:
        print("Hit the wall")
        scoreBoard.reset()
        snake.reset(3)


    for block in snake.snake_blocks[1:]:
        if snake.snake_blocks[0].distance(block) < 10:
            print("Hit the tail")
            scoreBoard.reset()
            snake.reset(3)

screen.exitonclick()