from turtle import Turtle, Screen


class Field(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.pensize(5)
        self.speed("fastest")

    def make_a_line(self):
        self.penup()
        self.goto(0, 350)
        self.setheading(270)
        self.pendown()
        for _ in range(24):
            self.forward(15)
            self.penup()
            self.forward(20)
            self.pendown()

