from turtle import Screen
from peddle import Peddle
from ball import Ball
from scoreboard import Scoreboard
s = Screen()
s.tracer(0)
ball = Ball()
s.bgcolor("black")
s.setup(800, 600)
s.title("Legendary Pong Game")

score = Scoreboard
rightp = Peddle((350, 0))
leftp = Peddle((-350, 0))


s.listen()
s.onkey(rightp.moveup, "Up")
s.onkey(rightp.movedown, "Down")
s.onkey(leftp.moveup, "w")
s.onkey(leftp.movedown, "s")
    


is_game_on = True

while is_game_on:
    s.update()
    ball.move()
    if ball.ycor() >= 260.0 or ball.ycor() <= -260.0:
        ball.bouncey()
    if ball.distance(rightp) < 50 and ball.xcor() > 320 or ball.distance(leftp) < 50 and ball.xcor() > -320:
        ball.bouncex()
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_score += 1
        score.r_point()


s.exitonclick()