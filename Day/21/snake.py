from turtle import Turtle, Screen
import time

MOVE_DISTANCE = 20


class Snake:
    

    def __init__(self, snake_init_size):
        self.screen = Screen()
        self.screen.setup(600, 600)
        self.screen.tracer(0)
        self.screen.bgcolor("black")
        self.screen.title("Snake Game")


        self.snake_blocks = []
        for x in range(0, -(snake_init_size * 20), -20):
            self.snake = Turtle("square")
            self.snake.penup()
            self.snake.color("white")
            self.snake.teleport(x, 0)
            self.snake_blocks.append(self.snake)

    
    def add_block(self):
        x = self.snake_blocks[-1].xcor()
        y = self.snake_blocks[-1].ycor()
        self.snake = Turtle("square")
        self.snake.penup()
        self.snake.color("white")
        self.snake.teleport(x, y)
        self.snake_blocks.append(self.snake)
        

    def move(self):
        for blocks in range(len(self.snake_blocks) - 1, 0, -1):
            new_x = self.snake_blocks[blocks - 1].xcor()
            new_y = self.snake_blocks[blocks - 1].ycor()
            self.snake_blocks[blocks].goto(new_x, new_y)
        self.snake_blocks[0].forward(MOVE_DISTANCE)


    def turn(self, key):
        current_heading = self.snake_blocks[0].heading()

        if key == "Up" and current_heading != 270:
            self.snake_blocks[0].setheading(90)
        elif key == "Right" and current_heading != 180:
            self.snake_blocks[0].setheading(0)
        elif key == "Down" and current_heading != 90:
            self.snake_blocks[0].setheading(270)
        elif key == "Left" and current_heading != 0:
            self.snake_blocks[0].setheading(180)


    def reset(self, snake_init_size):
        for block in self.snake_blocks:
            block.hideturtle()

        self.snake_blocks.clear()

        for x in range(0, -(snake_init_size * 20), -20):
            self.snake = Turtle("square")
            self.snake.penup()
            self.snake.color("white")
            self.snake.teleport(x, 0)
            self.snake_blocks.append(self.snake)


