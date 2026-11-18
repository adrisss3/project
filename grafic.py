from turtle import *
c = 0
bgcolor("black")
tracer(5)

while c < 300:
    fd(c)
    color("yellow")
    left(143)
    left(1)
    c += 1
    fd(c)
    color("greenyellow")
    right(350)
    radians()
    color("orange")
    right(30)
hideturtle()
done()