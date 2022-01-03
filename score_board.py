from turtle import Turtle

FONT = ("Courier New", 25, "normal")
CENTER = 'center'


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as data:
            self.high_score = int(data.read())

        self.penup()
        self.color('white')
        self.goto(0, 260)
        self.hideturtle()
        self.penup()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', align=CENTER, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f'Game Over!', align=CENTER, font=FONT)

    def refresh_score(self):
        self.score += 1
        self.update_score()
