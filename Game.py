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

def window () :
    turtle.onscreenclick(None)

    window()

    tfood = turtle.Turtle()
    tfood.hideturtle()
    tfood.pu()
    tfood.speed(0)
    tfood.shape("square")
    tfood.color("red")

    tscore = turtle.Turtle()
    tscore.hideturtle()
    tscore.pu()
    tscore.speed(0)
    tscore.goto(100, -250)
    tscore.write("Score:" + str(a[0]), align="center", font=(10))

    while x > -210 and x < 210 and y > -210 and y < 210:
        if foodcoord[2] == 0:
            food(tfood)
            foodcoord[2] = 1
        turtle.onkey(u, "Up")
        turtle.onkey(l, "Left")
        turtle.onkey(r, "Right")
        turtle.onkey(d, "Down")
        turtle.listen()
        move()
        x = turtle.xcor()
        y = turtle.ycor()
        if x > foodcoord[0] * 20 - 5 and x < foodcoord[0] * 20 + 5 and y > foodcoord[1] * 20 - 5 and y < foodcoord[
            1] * 20 + 5:
            foodcoord[2] = 0
            tfood.clear()
            a[0] += 1
            tscore.clear()
            tscore.write("Score:" + str(a[0]), align="center", font=(10))
         if len(cpos) > 1:
             for i in range(1, len(cpos)):
                if x < cpos[i][0] + 5 and x > cpos[i][0] - 5 and y < cpos[i][1] + 5 and y > cpos[i][1] - 5:
                        tscore.clear()
                        tfood.clear()
                        gameover()
    tscore.clear()
    tfood.clear()
    gameover()


