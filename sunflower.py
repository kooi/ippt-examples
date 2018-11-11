import turtle
import math

tina = turtle.Turtle()
tina.shape('turtle')
tina.speed(0)
tina.penup()
tina.getscreen().colormode(255)
tina.hideturtle()

a0 = 137.5
c = 4

step = 1

#for n in range(1000):
#for c1 in range(0, 256, step):
for c2 in range(0, 256, 32):
    print(c2)
    for c3 in range(1, 256, step):
        n = c3
        angle = n * a0
        r = c * math.sqrt(n)
        tina.goto( r*math.cos(angle), r*math.sin(angle) )
        tina.pencolor(0, c2, c3)
        tina.dot()
