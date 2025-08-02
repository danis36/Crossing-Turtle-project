from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVING_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.setheading(90)
        self.go_to_start()

    def move(self):
        new_y = self.ycor() + MOVING_DISTANCE
        self.goto(0, new_y)

    def is_at_finish_line(self):
        if  self.ycor() > FINISH_LINE_Y:
            return True
        else:
            False

    def go_to_start(self):
        self.goto(STARTING_POSITION)

