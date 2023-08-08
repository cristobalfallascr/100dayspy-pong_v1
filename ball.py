from turtle import Turtle
import random
MOVE_DISTANCE = 10

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.color("white")
        self.speed("fastest")

    def roll(self):

        self.forward(MOVE_DISTANCE)

    def set_direction(self):
        radom_direction = random.randint(0, 360)
        if radom_direction not in range (80, 100) and radom_direction not in range (260, 290) :
            self.setheading(radom_direction)

    #Dectect colisions

    def bounce_on_board(self):


        bounce_direction = 360 - self.heading()
        self.setheading(bounce_direction)
    # # Quadrant 1
    #     if self.heading()  in range(0,360):
    #         bounce_direction = 360-self.heading()
    #         self.setheading(bounce_direction)
    # # Quadrant 2
    #     elif self.heading() in range (90,180):
    #         bounce_direction = random.randint(180, 270)
    #         self.setheading(bounce_direction)
    # # Quadrant 3
    #
    #     elif self.heading() in range(180, 270):
    #         bounce_direction = random.randint(90, 180)
    #         self.setheading(bounce_direction)
    #
    # # Quadrant 4
    #
    #     elif self.heading() in range(270, 360):
    #         bounce_direction = random.randint(0, 90)
    #         self.setheading(bounce_direction)

    def bounce_on_pads(self):
        # if self.heading() < 180:
        #     bounce_direction = 1- self.heading()
        #     self.setheading(bounce_direction)
        # else:
        #     bounce_direction = 1 - self.heading()
        #     bounce_direction = bounce_direction / 2 + self.heading()
        #     self.setheading(bounce_direction)


       #Player 2 Bounce
        if self.heading() in range(0, 180) and self.xcor() >0:
            bounce_direction = random.randint(110, 250)
            self.setheading(bounce_direction)

        elif self.heading() in range(180, 360) and self.xcor() >0:
            bounce_direction = random.randint(110, 250)
            self.setheading(bounce_direction)
        #Player 1 Bounce
        elif self.heading() in range(90, 270):
            range_choice = random.choice([(0,70),(290,360) ])
            bounce_direction = random.randint(*range_choice)
            self.setheading(bounce_direction)

    def reset_ball(self):
        self.goto(0,0)
        self.set_direction()

