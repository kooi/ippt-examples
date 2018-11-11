import turtle
import math

G = 100.00

class Planet:
    def __init__(self, sx, sy, vx, vy, ax, ay, m, color):
        self.sx = sx
        self.sy = sy
        self.vx = vx
        self.vy = vy
        self.ax = ax
        self.ay = ay
        self.mass = m
        self.color = color
        self.renderer = turtle.Turtle()
        self.renderer.shape("circle")
        self.renderer.penup()
        # set at correct place
        self.renderer.goto(self.sx, self.sy)
        # ...
        self.renderer.getscreen().bgcolor( 0, 0, .2 )
        self.renderer.pencolor("white")
        self.renderer.pendown()
        self.renderer.radians()
    
    def step(self, dt, suns):
        self.ax = 0
        self.ay = 0
        for s in suns:
            #should iterate over all suns
            a = self.getForce(s)/self.mass
            angle = self.getForceDirection(s)
            self.ax += a*math.cos(angle)
            self.ay += a*math.sin(angle)
        
        self.vx += self.ax*dt
        self.vy += self.ay*dt
        self.sx += self.vx*dt
        self.sy += self.vy*dt

#        print(a, angle, self.ax, self.ay, self.vx, self.vy, self.sx, self.sy)
#        print(self.ax, self.ay, self.vx, self.vy, self.sx, self.sy)
#        print(a, angle)


    def getForceDirection(self, sun):
        return self.renderer.towards(sun.sx, sun.sy)

    def getForce(self, sun):
        # get distance between
        dx = self.sx - sun.sx
        dy = self.sy - sun.sy
        # return Force on self
        rsq = dx*dx+dy*dy
#        print (rsq)
        return G * self.mass*sun.mass / rsq

    def show(self):
        self.renderer.fillcolor(self.color)
        self.renderer.goto(self.sx, self.sy)


p1   = Planet( 100.0, 0.0,  10.0,  100.0,  0.0, 0.0,       100.0, "blue")
p2   = Planet( 200.0, 0.0,  10.0,  100.0,  0.0, 0.0,     10000.0, "green")
p3   = Planet( 300.0, 0.0,  10.0,  100.0,  0.0, 0.0,     10000.0, "red")
sun = Planet(    0.0, 0.0,   0.0,  -0.01,  0.0, 0.0,    100000.0, "yellow")
T = 5000
dt = 0.01

sun.show()


for t in range(T):
    p1.step(dt, [sun, p2, p3])
    p2.step(dt, [sun, p1, p3])
    p3.step(dt, [sun, p1, p2])
    sun.step(dt, [p1, p2])
    p1.show()
    p2.show()
    p3.show()
    sun.show()
