from turtle import Turtle, Screen
import math


def get_input():
    print('y = kx + b')
    k = float(input('k: '))
    b = float(input('b: '))
    return k, b


def draw_graph(k, b):
    g = Turtle()
    g.speed(0)

    height = 3000
    width = 3000
    screen = Screen()
    screen.screensize(width, height)

    g.penup()
    g.back(3000)
    g.pendown()
    g.forward(6000)
    g.penup()
    g.back(3000)
    g.pendown()
    g.left(90)
    g.forward(3000)
    g.penup()
    g.back(6000)
    g.pendown()
    g.forward(3000)

    g.forward(b * 20)
    g.color('blue')

    kf = math.degrees(math.atan(k))
    g.right(kf)
    g.forward(2000)
    g.right(180)
    g.forward(4000)
    g.right(180)
    g.forward(4000)
    g.hideturtle()


if __name__ == '__main__':
    k, b = get_input()
    draw_graph(k, b)
    input("Press any key to exit ...")
