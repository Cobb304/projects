from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


def random_y():
    random_n = random.randint(-280, 280)
    return random_n


class CarManager(Turtle):


    def __init__(self, x):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 2)
        self.penup()
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.goto(x, random_y())
    
    
    def car_movement(self, speed):
        self.forward(speed)
