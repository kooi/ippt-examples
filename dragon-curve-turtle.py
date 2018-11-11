import turtle
tina = turtle.Turtle()
tina.shape("turtle")

def turn(i):
    left = (((i & -i) << 1) & i) != 0
    return 'L' if left else 'R'

def curve(iteration):
    return ''.join([turn(i + 1) for i in range(2 ** iteration - 1)])

tina.showturtle()
tina.hideturtle()
tina.speed(0)
i = 1
while True:
    if turn(i) == 'L':
        tina.circle(-4, 90, 36)
    else:
        tina.circle(4, 90, 36)
    i += 1
