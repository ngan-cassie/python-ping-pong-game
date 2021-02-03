
import turtle
import os 

# create a window 
wn = turtle.Screen()
wn.title("Ping Pong Game")
wn.bgcolor("pink")
wn.setup(width=800, height=600)
wn.tracer(0) 

# SCORE
scoreAnna = 0
scoreBob = 0 

# Bob's paddle 
paddleBob = turtle.Turtle()
paddleBob.speed(0)
paddleBob.shape("square")  
paddleBob.color("black")
paddleBob.shapesize(stretch_wid=5, stretch_len=1) 
paddleBob.penup()
paddleBob.goto(350,0) 

# Anna's paddle
paddleAnna = turtle.Turtle() 
paddleAnna.speed(0) 
paddleAnna.shape("square")
paddleAnna.color("black")
paddleAnna.shapesize(stretch_wid=5, stretch_len=1) 
paddleAnna.penup() 
paddleAnna.goto(-350, 0) 
# Ball
ball = turtle.Turtle()  
ball.speed(0)
ball.shape("square") 
ball.color("red")
ball.penup() 
ball.goto(0,0) 

# change in direction
ball.dx = 0.2
ball.dy = 0.2

# Scoreboard
pen = turtle.Turtle()
pen.speed(0) 
pen.color("red")
pen.penup() 
pen.hideturtle()
pen.goto(0, 260)
pen.write("ANNA: 0  BOB: 0", align = "center", font = ("Courier",24,"normal"))

# Function
def Bob_up():
    y = paddleBob.ycor() 
    y += 20 
    paddleBob.sety(y) 
def Bob_down():
    y = paddleBob.ycor() 
    y -= 20 
    paddleBob.sety(y) 
def Anna_up():
    y = paddleAnna.ycor() 
    y += 20 
    paddleAnna.sety(y) 
def Anna_down():
    y = paddleAnna.ycor()
    y -= 20 
    paddleAnna.sety(y) 
    
# Keyboard binding
wn.listen() 
wn.onkeypress(Bob_up, "Up")
wn.onkeypress(Bob_down, "Down")
wn.onkeypress(Anna_up, "w")
wn.onkeypress(Anna_down, "s")

# MAIN GAME LOOP
while True:
    wn.update()
   
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy) 
    
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1  
        os.system("afplay bounce.wav&")
    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1  
        os.system("afplay bounce.wav&")
    if ball.xcor() > 390:
        ball.goto(0,0) 
        ball.dx *= -1
        scoreAnna += 1 
        pen.clear()
        pen.write("ANNA: {}  BOB: {}".format(scoreAnna, scoreBob), align = "center", font = ("Courier",24,"normal"))
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        scoreBob += 1 
        pen.clear() 
        pen.write("ANNA: {}  BOB: {}".format(scoreAnna, scoreBob), align = "center", font = ("Courier",24,"normal"))

    if ball.xcor() > 330 and ball.xcor() < 350 and ball.ycor() < paddleBob.ycor() + 40 and ball.ycor() > paddleBob.ycor() - 40: 
        ball.setx(330)
        ball.dx *= -1 
        os.system("afplay bounce.wav&")
    if ball.xcor() < -330 and ball.xcor() > -350 and ball.ycor() < paddleAnna.ycor() + 40 and ball.ycor() > paddleAnna.ycor() - 40: 
        ball.setx(-330)
        ball.dx *= -1
        os.system("afplay bounce.wav&")
