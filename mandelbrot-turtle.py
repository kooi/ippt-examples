import turtle
from PIL import Image
import io

res = 3

tina = turtle.Turtle()
tina.shape('turtle')
tina.speed(0)
tina.penup()
tina.getscreen().colormode(255)


def z2(a, b):
    return (a*a-b*b, 2*a*b)


def zn(z, c):
    return ( z2(z[0], z[1])[0] + c[0], z2(z[0], z[1])[1] + c[1] )


def z_abs_sqr(z):
    return z[0]*z[0] + z[1]*z[1]


def plot_point( x, y, c ):
    tina.goto(x, y)
    tina.pencolor(c)
    tina.dot(size=res)


#for a in range(-200, 100, res):
for a in range(-150, 100, res):
#    for b in range(-150, 150, res):
    for b in range(-125, 125, res):
        z = (0,0)
        for i in range(0, 256, 1):
            z = zn( z, (a/100., b/100.) )
            if z_abs_sqr(z)>4.0:
                break
        if i == 255:
            plot_point(a, b, (0, 0, 0))
        else:
            plot_point(a, b, (i, i, 255-i))

from PIL import Image
import io

ps = tina.getscreen().getcanvas().postscript()
img = Image.open(io.BytesIO(ps.encode('utf-8')))
img.save('mandelbrot-turtle.png')

