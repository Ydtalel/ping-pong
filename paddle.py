from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x, y)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


# STARTING_POSITION = [(-490, -20), (-490, 0), (-490, 20)]
# MOVE_DISTANCE = 20
# UP = 90
# DOWN = 270
#
#
#
# class Paddle(Turtle):
#
#     def __init__(self):
#         super().__init__()
#         self.segments = []
#         self.create_paddle_1()
#         self.head = self.segments[0]
#         self.tail = self.segments[2]
#         self.speed(1000)
#
#
#
#     def create_paddle_1(self):
#         for position in STARTING_POSITION:
#             self.add_segment(position)
#
#     def add_segment(self, position):
#         new_segment = Turtle(shape="square")
#         new_segment.penup()
#         new_segment.color("white")
#         new_segment.goto(position)
#         self.segments.append(new_segment)
#
#     def move_up(self):
#         for seg_num in range(len(self.segments) - 1, 0, -1):
#             new_x = self.segments[seg_num - 1].xcor()
#             new_y = self.segments[seg_num - 1].ycor()
#             self.segments[seg_num].goto(new_x, new_y)
#         self.head.fd(MOVE_DISTANCE)
#
#     def move_down(self):
#         for seg_num in range(0, 2, 1):
#             new_x = self.segments[seg_num + 1].xcor()
#             new_y = self.segments[seg_num + 1].ycor()
#             self.segments[seg_num].goto(new_x, new_y)
#         self.tail.fd(MOVE_DISTANCE)
#
#     def up(self):
#         for self.segment in self.segments:
#             self.head.setheading(UP)
#             if self.head.ycor() < 330:
#                 self.move_up()
#
#     def down(self):
#         for self.segment in self.segments:
#             self.tail.setheading(DOWN)
#             if self.tail.ycor() > -340:
#                 self.move_down()
#
