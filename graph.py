from turtle import *
import math


g = Turtle()

g.speed(0)

height = 3000
width = 3000
screen = Screen()
screen.screensize(width, height)

g.pu()
g.bk(3000)
g.pd()
g.fd(6000)
g.pu()
g.bk(3000)
g.pd()
g.lt(90)
g.fd(3000)
g.pu()
g.bk(6000)
g.pd()
g.fd(3000)


print('y = kx + b')

k = float(input('k: '))

b = float(input('b: '))

g.forward(b * 20)

g.color('blue')

kf = math.degrees(math.atan(k))
g.right(kf)


g.fd(2000)
g.rt(180)
g.fd(4000)
g.rt(180)
g.fd(4000)

input("Press any key to exit ...")