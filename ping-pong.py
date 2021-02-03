# use module "turtle" to add graphics to our window 
import turtle
import os 
# create a window 
wn = turtle.Screen()
wn.title("Ping Pong Game")
wn.bgcolor("pink")
wn.setup(width=800, height=600)
# stop the window from updating
wn.tracer(0) 

# SCORE
scoreAnna = 0
scoreBob = 0 

# Paddle A
paddleBob = turtle.Turtle() # Turtle: class name 
paddleBob.speed(0) # speed of animation - set the screen to maximum speed 
paddleBob.shape("square") # use built-in shape 
paddleBob.color("black")
paddleBob.shapesize(stretch_wid=5, stretch_len=1) # wid = height
paddleBob.penup() # no drawing line when we move 
paddleBob.goto(350,0) # start at (x: -350, y: center of the screen) 
# Paddle B
paddleAnna = turtle.Turtle() # Turtle: class name 
paddleAnna.speed(0) # speed of animation - set the screen to maximum speed 
paddleAnna.shape("square") # use built-in shape 
paddleAnna.color("black")
paddleAnna.shapesize(stretch_wid=5, stretch_len=1) # wid = height
paddleAnna.penup() # no drawing line when we move 
paddleAnna.goto(-350, 0) 
# Ball
ball = turtle.Turtle() # Turtle: class name 
ball.speed(0) # speed of animation - set the screen to maximum speed 
ball.shape("square") # use built-in shape 
ball.color("red")
ball.penup() # no drawing line when we move 
ball.goto(0,0) 
# d: change, every time the ball moves, it moves 2 up and 2 right 
ball.dx = 0.2
ball.dy = 0.2

# Pen
pen = turtle.Turtle()
pen.speed(0) 
pen.color("red")
pen.penup() 
pen.hideturtle()
pen.goto(0, 260)
pen.write("ANNA: 0  BOB: 0", align = "center", font = ("Courier",24,"normal"))

# Function
def Bob_up():
    y = paddleBob.ycor() # ycor() returns the y coordinate 
    y += 20 # add 20px to the y coords
    paddleBob.sety(y) 
def Bob_down():
    y = paddleBob.ycor() # ycor() returns the y coordinate 
    y -= 20 # add 20px to the y coords
    paddleBob.sety(y) 
def Anna_up():
    y = paddleAnna.ycor() # ycor() returns the y coordinate 
    y += 20 # add 20px to the y coords
    paddleAnna.sety(y) 
def Anna_down():
    y = paddleAnna.ycor() # ycor() returns the y coordinate 
    y -= 20 # add 20px to the y coords
    paddleAnna.sety(y) 
    
# Keyboard binding
wn.listen() # listen for keyboard input
wn.onkeypress(Bob_up, "Up")
wn.onkeypress(Bob_down, "Down")
wn.onkeypress(Anna_up, "w")
wn.onkeypress(Anna_down, "s")

# MAIN GAME LOOP
while True:
    # every time the loop runs, it updates the screen 
    wn.update()
    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy) 
    # border checking 
    # once it gets to a certain point, the ball bounces  
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 # reverse the direction 
        os.system("afplay bounce.wav&")
    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1 # reverse the direction 
        os.system("afplay bounce.wav&")
    if ball.xcor() > 390:
        ball.goto(0,0) # the padlde misses the ball 
        ball.dx *= -1
        scoreAnna += 1 
        pen.clear() # so that the number isn't printed on top of the other 
        pen.write("ANNA: {}  BOB: {}".format(scoreAnna, scoreBob), align = "center", font = ("Courier",24,"normal"))
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        scoreBob += 1 
        pen.clear() 
        pen.write("ANNA: {}  BOB: {}".format(scoreAnna, scoreBob), align = "center", font = ("Courier",24,"normal"))
    # paddle and ball collisions 
    if ball.xcor() > 330 and ball.xcor() < 350 and ball.ycor() < paddleBob.ycor() + 40 and ball.ycor() > paddleBob.ycor() - 40: 
        ball.setx(330)
        ball.dx *= -1 
        os.system("afplay bounce.wav&")
    if ball.xcor() < -330 and ball.xcor() > -350 and ball.ycor() < paddleAnna.ycor() + 40 and ball.ycor() > paddleAnna.ycor() - 40: 
        ball.setx(-330)
        ball.dx *= -1
        os.system("afplay bounce.wav&")
