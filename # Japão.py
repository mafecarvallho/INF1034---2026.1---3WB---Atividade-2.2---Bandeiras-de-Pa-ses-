
import turtle
from time import sleep


from turtle import *

# Japão 

c = Turtle()

c.pu()
c.goto(-150 , 0)
c.down()

for _ in range(2):
    c.fd(300)
    c.left(90)
    c.fd(200)
    c.left(90)

c.pu()
c.goto(0,50)
c.down()
c.color('red')
c.begin_fill()
c.circle(50)
c.end_fill()

sleep(5)
c.clear()


# bandeira a irlanda

c.color('black')
c.pu()
c.goto(-150,0)
c.down()

for _ in range(2):
    c.fd(300)
    c.left(90)
    c.fd(200)
    c.left(90)

c.pu()
c.goto(-50, 0)
c.down()
c.begin_fill()
c.fillcolor('green')

for _ in range(2):
    c.left(90)
    c.fd(200)
    c.left(90)
    c.fd(100)

c.end_fill()

c.pu()
c.goto(150, 0)
c.down()
c.begin_fill()
c.fillcolor('orange')

for _ in range(2):
    c.left(90)
    c.fd(200)
    c.left(90)
    c.fd(100)

c.end_fill()

sleep(5)
c.clear()


# bandeira niger


c.color('black')
c.pu()
c.goto(-150,0)
c.down()

for _ in range(2):
    c.fd(300)
    c.left(90)
    c.fd(210)
    c.left(90)


c.pu()
c.goto( - 150, 70)
c.down()

c.begin_fill()
c.fillcolor('green')

for _ in range(2):
    c.fd(300)
    c.right(90)
    c.fd(70)
    c.right(90)

c.end_fill()

c.pu()
c.goto(  - 150, 140)
c.down()

c.begin_fill()
c.fillcolor('#FF8C00')

for _ in range(2):
    c.fd(300)
    c.left(90)
    c.fd(70)
    c.left(90)

c.end_fill()

c.pu()
c.goto(0 , 75)
c.down()
c.begin_fill()
c.fillcolor('#FF8C00')
c.circle(30)
c.end_fill()


sleep(5)
c.clear()

# bandeira emirados arabes

c.color('black')
c.pu()
c.goto(-150,0)
c.down()

for _ in range(2):
    c.fd(300)
    c.left(90)
    c.fd(210)
    c.left(90)


c.pu()
c.goto( - 150, 70)
c.down()

c.begin_fill()
c.fillcolor('black')

for _ in range(2):
    c.fd(300)
    c.right(90)
    c.fd(70)
    c.right(90)

c.end_fill()

c.pu()
c.goto(  - 150, 140)
c.down()

c.begin_fill()
c.fillcolor('#006400')

for _ in range(2):
    c.fd(300)
    c.left(90)
    c.fd(70)
    c.left(90)

c.end_fill()

c.pu
c.goto(-150,0)
c.color('black')
c.begin_fill()
c.fillcolor('#8B0000')
c.right(180)

for _ in range(2):
    c.fd(100)
    c.right(90)
    c.fd(210)
    c.right(90)

c.end_fill()

sleep(5)
c.clear()


# Bandeira de bahamas

c.pu()
c.goto(-150 , 0)
c.down()
c.color('#4682B4')
c.begin_fill()

for _ in range(2):
    c.fd(300)
    c.left(90)
    c.fd(210)
    c.left(90)

c.end_fill()

c.pu()
c.goto( - 150 , 70)
c.down()
c.color('yellow')
c.begin_fill()

for _ in range(2):
    c.fd(300)
    c.left(90)
    c.fd(70)
    c.left(90)

c.end_fill()


c.pu()
c.goto( - 150 , 0)
c.down()
c.color('black')
c.begin_fill()

c.left(90)
for _ in range(3):
    c.fd(210)
    c.right(120)
c.end_fill()

sleep(5)
c.clear()




mainloop()
