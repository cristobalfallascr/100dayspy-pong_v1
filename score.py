from turtle import Turtle
ALINGMENT = 'center'
FONT = ("Consolas", 25, "normal")

class ScoreBoard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.player = position
        self.score = 0
        self.penup()
        self.set_position(self.player)
        self.color('white')
        self.hideturtle()
        self.update_scoreboard(self.player)


    def set_position(self,player):
        if player == 1:
            self.goto(-40,220)
        else:
            self.goto(20,220)
    def update_scoreboard(self, player):
        self.write(f" {self.score}", align=ALINGMENT, font=FONT)
    def increase_score(self, player):
        self.score += 1
        self.clear()
        self.update_scoreboard(player)

    def game_over(self):
        self.goto(0,0)
        self.color('red')
        self.write("GAME OVER!", align=ALINGMENT, font=FONT)
