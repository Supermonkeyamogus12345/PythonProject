import turtle as t

def changepoztisision (x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def wood (o):
    o=o+20
    changepoztisision(x=o, y=-360)
    t.left(90)
    t.color('brown4')
    t.end_fill()
    t.begin_fill()
    t.forward(85)
    t.color('green')
    t.begin_fill()
    t.right(90)
    t.circle(40)
    t.end_fill()

def piramid (color,high):
    t.color(color)
    t.begin_fill()
    t.forward(high)
    t.left(120)
    t.forward(high)
    t.left(120)
    t.forward(high)
    t.left(120)
    t.end_fill()

def pofi0sdfcx (ugol,high):
    t.right(ugol)
    t.forward(high)
    t.right(ugol)
    t.forward(high)
    t.right(ugol)
    changepoztisision(x=-100, y=200)
    t.right(ugol)
    t.forward(high)
    t.right(ugol)
    t.forward(high)
    t.right(ugol)
    changepoztisision(x=-50, y=150)
    t.right(ugol)
    t.forward(high)
    t.right(ugol)
    t.forward(high)
    t.done()

def white(cirkle):
    for i in range(3):
        i = i + 20
        changepoztisision(x=i, y=250)
        t.color('white')
        t.begin_fill()
        t.circle(cirkle)
        t.end_fill()

