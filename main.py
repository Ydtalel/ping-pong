import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

time

go_on = True
screen = Screen()
paddle = Paddle(350, 0)
paddle_2 = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.listen()
screen.tracer(0)

screen.onkey(paddle.move_up, "Up")
screen.onkey(paddle.move_down, "Down")
screen.onkey(paddle_2.move_up, "w")
screen.onkey(paddle_2.move_down, "s")

s = 0.090

while go_on:
    time.sleep(s)
    screen.update()
    ball.speed(s)
    ball.go()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle) < 50 and ball.xcor() > 320 or ball.distance(paddle_2) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        if s > 0.010:
            s -= 0.005

    if ball.xcor() > 350:
        ball.go_opposite()
        scoreboard.l_point()
        s = 0.090

    if ball.xcor() < -350:
        ball.go_opposite()
        scoreboard.r_point()
        s = 0.090

# field.make_a_line()
# # screen.update()
# # screen.tracer(100, 25)
# screen.onkey(paddle_1.up, "Up")
# screen.onkey(paddle_1.down, "Down")
# ball.start()
#
# while go_on:
#     # screen.update()
#     # time.sleep(0.1)
#     # screen.tracer(100, 25)
#     ball.go()
#     if paddle_1.head.distance(ball) < 20:
#         ball.right(90)
#         ball.go()


# screen.onkey(paddle_1.up, "Up")
# screen.onkey(paddle_1.down, "Down")


screen.exitonclick()
