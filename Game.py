import turtle
import random

head = [0]

#score
a = [0]
b = [0]

#food coord
foodcoord = [0,0,0]

#cposition
cpos = []

def home (x,y) :
    x = 0
    y = 0
    a[0] = 0
    b[0] = 0
    head[0] = 0
    foodcoord[2] = 0
    cpos[:] =  []
    turtle.hideturtle()
    turtle.clear()
    turtle.pu()
    turtle.color("red")
    turtle.goto(0,0)
    turtle.write("play")
    turtle.title("Snake Game")
    turtle.onscreenclick(start)
    turtle.mainloop()

