from turtle import Turtle

FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.teleport(-285, 265)
        self.scoreboard_update()

    def scoreboard_update(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", font=FONT)


    def plusOne(self):
        self.level += 1
        self.scoreboard_update()


    def game_over(self):
        self.level = 1
        self.scoreboard_update()
        self.home()
        self.write(arg="GAME OVER", align="center", font=("Courier", 40, "bold"))

