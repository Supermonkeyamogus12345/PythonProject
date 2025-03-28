import turtle as t
x=0
k=0
i=0
o=-200
from function import changepoztisision
from function import wood
from function import piramid
from function import pofi0sdfcx
from function import white
t.speed(1000)
changepoztisision (x=-950,y=-100)
t.color('antiquewhite')
t.begin_fill()
t.forward(2000)
t.right(90)
t.forward(1000)
t.right(90)
t.forward(2000)
t.left(90)
t.forward(1000)
t.end_fill()
t.penup()
t.goto(-950,-100)
changepoztisision (x=-950,y=-100)
t.color('lightblue')
t.begin_fill()
t.left(90*2)
t.forward(2000)
t.right(90)
t.forward(2000)
t.right(90)
t.forward(2000)
t.left(90)
t.forward(2000)
t.end_fill()
changepoztisision (x=300,y=-100)
piramid (color='goldenrod',high=500)
changepoztisision (x=200,y=-100)
piramid (color='purple',high=300)
changepoztisision (x=100,y=-100)
piramid (color='green',high=150)
for i in range(4):
    wood(o=o)
    o=o+100
changepoztisision (x=-400,y=350)
t.color('yellow')
t.begin_fill()
t.circle(150)
t.end_fill()
white(cirkle=50)
changepoztisision (x=-200,y=250)
t.color('black')
pofi0sdfcx (ugol=120,high=40)