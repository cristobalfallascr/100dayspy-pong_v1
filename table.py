DIMENSION = (200, 200)
from turtle import Turtle

class Table():
    def __init__(self):

        self.create_net()
        self.create_borders()


    def create_net(self):
        net = Turtle()
        net.hideturtle()
        net.penup()
        net.goto(0,200)
        net.pensize(5)
        net.color('green')
        net.setheading(270)
        for i  in range(0,20,1):
            net.pendown()
            net.forward(10)

            net.penup()
            net.forward(10)



    def create_borders(self):
        border = Turtle()

        border.hideturtle()
        border.penup()
        border.goto(-190,-190)
        border.pensize(5)
        border.color('gray')

        for i  in range(0,4,1):
            border.pendown()
            border.forward(400)
            border.left(90)
            border.penup()
            border.forward(400)
            border.left(90)




