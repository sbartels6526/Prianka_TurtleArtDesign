import turtle
from myShape import *
turtle.colormode(255)
turtle.bgcolor("black")
bob = turtle.Turtle()
bob.speed(0)
turtle.tracer(0)

for i in range(180):
    bob.pencolor("white")
    bob.forward(1000000)
    bob.right(50)
    bob.forward(200000)
    bob.left(120)
    bob.forward(500000)
    bob.right(30)
    
    bob.penup()
    bob.setposition(0,0)
    bob.pendown()
    
    bob.right(2)

bob.color(255, 0, 12)
move(bob,-10,-156)
polygon(bob,10,100)
bob.color(0,0,0)
move(bob,-8,-135)
polygon(bob,8.5,100)

bob.color(255,252,119)
move(bob,-150,-40)
star(bob,287,5)

bob.color(0,0,0)
move(bob,-116,-31)
star(bob,220,5)

bob.color(255,252,119)
move(bob,-82,-20)
star(bob,153,5)

bob.color(0,0,0)
move(bob,-61,-15)
star(bob,110,5)

bob.color(255,252,119)
move(bob,-46,-11)
star(bob,80,5)

bob.color(0,0,0)
move(bob,-31,-7)
star(bob,50,5)

bob.color(255,252,119)
move(bob,-21,-4)
star(bob,30,5)

bob.color(0,0,0)
move(bob,-16,-2)
star(bob,20,5)

bob.color(255,0,12)
move(bob,215,45)
polygon(bob,5,100)
bob.color(0,0,0)
move(bob,217,55)
polygon(bob,4.25,100)
bLT(bob,250,50)

bob.color(255, 0, 12)
move(bob,-285,76)
polygon(bob,5,100)
bob.color(0,0,0)
move(bob,-275,84)
polygon(bob,4.25,100)
bLT(bob,-267,59)
