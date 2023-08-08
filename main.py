from turtle import Screen
import time
from pad import Pad
from players import Player
from table import Table
from ball import Ball
from score import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")

screen.title("Pong")
screen.tracer(0)

table = Table()
ball = Ball()
player_one = Pad(1)
player_one_score = ScoreBoard(1)
player_two = Pad(2)
player_two_score = ScoreBoard(2)


screen.listen()
screen.onkey(player_one.up, "q")
screen.onkey(player_one.down,"a")
screen.onkey(player_two.up, "Up")
screen.onkey(player_two.down,"Down")

game_is_on= True
ball.set_direction()
while game_is_on:

    screen.update()
    time.sleep(0.05)
    ball.roll()


    #Colision with Boards
    if ball.ycor() >= 200 or ball.ycor() <= -180:
        ball.bounce_on_board()




    # Collision with player 1

    for pad_segment in player_one.pad:
        if ball.distance(pad_segment) <10:
            ball.bounce_on_pads()

            print("collision with Pad one" +str(pad_segment))
            print(ball.heading())

    # Collision with player 2

    for pad_segment in player_two.pad:
        if ball.distance(pad_segment) <10:
            ball.bounce_on_pads()

            print("collision with Pad two"+str(pad_segment))
            print(ball.heading())


    if ball.xcor() >220:
        print("player one scores")
        # game_is_on=  False
        player_one_score.increase_score(1)
        time.sleep(1)
        ball.reset_ball()
    if ball.xcor() <-220:
        print("player two scores")
        # game_is_on=  False
        player_two_score.increase_score(2)
        time.sleep(1)
        ball.reset_ball()
screen.exitonclick()