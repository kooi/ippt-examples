import turtle
tina = turtle.Turtle()
tina.shape("turtle")

tina.speed(0)
turtle.Screen().tracer(8)

def sierpinski_arrowhead_curve( order, length):
        curve( order, length, +60)

def curve(order, length, angle):
    if order == 0:
        tina.forward(length)
    else:
        curve( order - 1, length / 2, - angle);
        tina.right( + angle);
        curve( order - 1, length / 2, + angle);
        tina.right( + angle);
        curve( order - 1, length / 2, - angle);

tina.setheading(0)
n = 10
colors = [(0,x,0) for x in range(200, 100, (100-200)/n)]
for i in range(2, 1+n, 1):
    tina.penup()
    tina.goto(-128,-100)
    tina.pendown()
    tina.pencolor( colors[i%len(colors)] )
    tina.setheading((i%2)*60)
    sierpinski_arrowhead_curve(i, 256)
