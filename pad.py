from turtle import Turtle
MOVE_DISTANCE = 30
UP=90
DOWN=270
P1_INITIAL_POSTION = -200
P2_INITIAL_POSITION= 260

class Pad:
    def __init__(self, position):
        self.position = position
        self.pad = []
        self.create_pad()
        self.upper = self.pad[-1]
        self.lower = self.pad[0]





    def create_segment(self):
        for segment in range(0,5,1):
            p = Turtle(shape="square")
            p.penup()
            p.shapesize(stretch_len=1, stretch_wid=0.5,)
            p.color('orange')
            p.setheading(UP)
            # p.get_position()
            p.pos = ""
            self.pad.append(p)


    def set_position(self, position):
        y_pos = 0

        if position == 1:

            for segment in self.pad:

                segment.goto(-180, y_pos)
                y_pos += 10


        else:

            for segment in self.pad:
                segment.goto(180, y_pos)
                y_pos += 10

    def create_pad(self):

        self.create_segment()
        self.set_position(self.position)

        # self.pad = Turtle(shape="square")
        # self.pad.penup()
        # self.pad.shapesize(stretch_len=3, stretch_wid=0.5,)
        # self.pad.color('orange')
        # self.get_position()
        # self.pos =""

    #set paddle position (player)
    # def get_position(self):
    #     self.pos = self.pad.pos()
    #     return self.pos



    #detect table limit

    def detect_upper(self):
        if self.pad[-1].ycor() >= 170:
            return True

    def detect_lower(self):
        if  self.pad[1].ycor() <=-170:
            return True

    # Pad movements
    def up(self):


        if self.detect_upper()!= True:
            for segment in self.pad:

                segment.setheading(UP)
                segment.forward(MOVE_DISTANCE)


    def down(self):


        if self.detect_lower() != True:
            for segment in self.pad:
                segment.setheading(DOWN)
                segment.forward(MOVE_DISTANCE)

