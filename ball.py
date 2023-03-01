from turtle import Turtle

s = 1
# import random
#
# ANGLE_LEFT = [120, 125, 130, 135, 140, 145, 150]
# ANGLE_RIGHT = [30, 35, 40, 45, 50, 55, 60]

# go_on = Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.step_x = 10
        self.step_y = 10

    def go(self):
        new_x = self.xcor() + self.step_x
        new_y = self.ycor() + self.step_y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.step_y *= -1

    def bounce_x(self):
        self.step_x *= -1


    def go_opposite(self):
        self.goto(0, 0)
        self.bounce_x()





