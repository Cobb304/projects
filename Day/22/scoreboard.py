from turtle import Turtle


class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0

        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.teleport(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 60, "bold"))
        self.teleport(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 60, "bold"))


    def plusOne(self, x):
        if x > 0:
            self.l_score += 1
        elif x < 0:
            self.r_score +=1

        self.clear()
        self.update_scoreboard()