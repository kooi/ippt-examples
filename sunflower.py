import turtle
import math

tina = turtle.Turtle()
tina.shape('turtle')
tina.speed(0)
tina.penup()
tina.hideturtle()
turtle.Screen().tracer(10)

a0 = 137.5
c = 8

step = 1

for c2 in range(0, 256, 32):
    for c3 in range(1, 256, step):
        n = c3
        angle = n * a0
        r = c * math.sqrt(n)
        tina.goto( r*math.cos(angle), r*math.sin(angle) )
        tina.pencolor(256-c2, c2, c3)
        tina.dot()
