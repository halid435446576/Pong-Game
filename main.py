from turtle import Screen
from paddle import Paddle, NewPaddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.listen()
screen.tracer(0)

r_paddle = Paddle()
l_paddle = NewPaddle()
ball = Ball()
score_board = ScoreBoard()


screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.speed(0)
        ball.bounce_y()

    if (ball.xcor() >= 340 and ball.distance(r_paddle.paddle) < 50 or ball.xcor() <= -340 and
            ball.distance(l_paddle.paddle) < 50):

        ball.bounce_x()

    if ball.xcor() >= 380:
        score_board.l_score += 1
        score_board.update_score()
        ball.pass_by()
    if ball.xcor() <= -380:
        score_board.r_score += 1
        score_board.update_score()
        ball.pass_by()

screen.exitonclick()
