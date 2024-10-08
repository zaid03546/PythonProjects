from turtle import Turtle
ALIGMENT="center"
FONT=("Arial", 10, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("Data.txt") as data:
            self.high_score=int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0,y=280)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"SCORE: {self.score} High Score:{self.high_score}" , align=ALIGMENT, font=FONT)


    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("Data.txt",mode="w") as data:
                data.write(f"{self.high_score}")
        self.score=0
        self.update_score()


    # def game_over(self):
    #     self.goto(0,0)
        # self.write(f"GAME OVER !!!\nYou Have Hit The Wall\nYour Score Is: {self.score}", align=ALIGMENT, font=("Arial", 20, "normal"))
    def increase_score(self):
        self.score+=1
        self.update_score()



