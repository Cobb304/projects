from turtle import Screen, Turtle

PADDLE_SPEED = 50

class Paddle(Turtle):


    def __init__(self, x):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(5, 1)
        self.teleport(x, 0)


    def keybinds(self, key):
        if key == "Up" or key == "w":
            new_y = self.ycor() + PADDLE_SPEED
            self.goto(self.xcor(), new_y)
        elif key == "Down" or key == "s":
            new_y = self.ycor() - PADDLE_SPEED
            self.goto(self.xcor(), new_y)
