import turtle
tina = turtle.Turtle()
tina.shape("turtle")
tina.speed(0)

def maakvierhoek():
    for i in range(4):
        tina.right(90)
        tina.forward(100)

for j in range(6):
    for i in ['red', 'green', 'blue','red', 'green', 'blue','red', 'green', 'blue''red', 'green', 'blue']:
        tina.pencolor(i)
        maakvierhoek()
        tina.right(30)
    tina.right(5)
