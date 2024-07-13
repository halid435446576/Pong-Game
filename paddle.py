from turtle import Turtle


class Paddle:
    def __init__(self):
        self.paddle = Turtle()
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.resizemode("user")
        self.paddle.shapesize(1, 5)
        self.paddle.penup()
        self.paddle.setpos(350, 0)
        self.paddle.setheading(90)

    def up(self):
        self.paddle.forward(20)

    def down(self):
        self.paddle.backward(20)


class NewPaddle(Paddle):
    def __init__(self):
        super().__init__()
        self.paddle.setpos(-350, 0)

    def up(self):
        super().up()

    def down(self):
        super().down()
