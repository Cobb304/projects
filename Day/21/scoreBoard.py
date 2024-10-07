from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Roboto", 12, "bold")

class ScoreBoard(Turtle):


    def __init__(self):
        self.score = 0
        with open("Day/21/data.txt") as file:
            self.high_score = int(file.read())
            
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.teleport(0, 270)
        self.update_board()


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

            with open("Day/21/data.txt", "w") as file:
             file.write(str(self.high_score))

        self.score = 0
        self.update_board()


    def update_board(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, ALIGNMENT, FONT)


    def plusOne(self):
        self.score += 1
        self.update_board()
    