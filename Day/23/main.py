import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from os import system
system("cls")


def random_x():
    random_n = random.randint(315, 915)
    return random_n


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
cars = []

screen.listen()
screen.onkey(player.move_up, "Up")

car_density = 20
car_speed = 5
game_is_on = True
second_gen = False
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if len(cars) < car_density and not second_gen:
        cars.append(CarManager(random_x()))
    elif len(cars) < car_density:
        cars.append(CarManager(315))

    for car in cars:
        if car.distance(player) < 25:
            game_is_on = False
            scoreboard.game_over()

        car.car_movement(car_speed)

        if car.xcor() < -320:
            car.hideturtle()
            cars.remove(car)
            second_gen = True
            

    if player.ycor() > 280:
        player.reset()
        for car in cars:
            car.hideturtle()
        cars = []
        car_density += 3
        car_speed += 2
        second_gen = False
        scoreboard.plusOne()
        

screen.exitonclick()