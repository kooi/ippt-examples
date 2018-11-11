import turtle
tina = turtle.Turtle()
tina.shape("turtle")

tina.speed(0)

def sierpinski_arrowhead_curve( order, length):
    # If order is even we can just draw the curve.
    if order %2 == 0:
        curve( order, length, +60)
    else: #order is odd
        tina.right( +60);
        curve( order, length, -60);

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
#colors = ['dark red', 'dark green', 'dark blue', 'limegreen']
#for i in range(2, 7, 1):
#    tina.pencolor( colors[i%len(colors)] )
#    sierpinski_arrowhead_curve(i, 128)


tina.begin_poly()
sierpinski_arrowhead_curve(5, 128)
tina.end_poly()
print(tina.get_poly())

tina.getscreen().exitonclick()
