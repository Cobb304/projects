from turtle import Turtle
import random

ball_speed = 10
BALL_START_ANGLE = [-135, -45, 45, 135]


class Ball(Turtle):


    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.current_heading = random.choice(BALL_START_ANGLE)
    

    def ball_movement(self):
        self.setheading(self.current_heading)
        self.forward(ball_speed)


    def wall_bounce(self):
        self.current_heading = self.current_heading % 360
        
        if self.heading() >= 0 and self.heading() < 90:
            self.current_heading -= 90
        elif self.heading() >= 90 and self.heading() < 180:
            self.current_heading += 90
        elif self.heading() >= 180 and self.heading() < 270:
            self.current_heading -= 90
        elif self.heading() >= 270 and self.heading() < 360:
            self.current_heading += 90


    def paddle_bounce(self):
        global ball_speed
        ball_speed += 0.5
        self.current_heading = self.current_heading % 360

        if self.heading() >= 0 and self.heading() < 90:
            self.current_heading += 90
        elif self.heading() >= 90 and self.heading() < 180:
            self.current_heading -= 90
        elif self.heading() >= 180 and self.heading() < 270:
            self.current_heading += 90
        elif self.heading() >= 270 and self.heading() < 360:
            self.current_heading -= 90
            

    def ball_out(self):
        global ball_speed
        ball_speed = 10
        self.home()
        self.current_heading = random.choice(BALL_START_ANGLE)

