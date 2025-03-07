from turtle import Turtle

FONT = ('Arial', 12, 'normal')
ALIGNMENT = "center"

class Score(Turtle):


    def __init__(self):
        super().__init__()
        self.score = 0
        with open("./part3/snake_game/snake_data.txt") as data:
            self.highscore = int(data.read())
        self.teleport(x=0, y=280)
        self.hideturtle()
        self.color("white")
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("./part3/snake_game/snake_data.txt", "w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update()

    # def game_over(self):
    #     self.teleport(0, 20)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
    #     self.teleport(0, -20)
    #     self.write(f"Your score was: {self.score}", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1

        self.update()
        