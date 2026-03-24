

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


# bandeira a irlanda - bandeira usando funções do extra

def f(cor):
    c.color(cor)
    c.begin_fill()
    for _ in range(2):
         c.left(90)
         c.fd(200)
         c.left(90)
         c.fd(100)
    c.end_fill()
  
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
f('green')

c.pu()
c.goto(150, 0)
c.down()
f('orange')

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

c.right(180)
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


# bandeira do senegal


c.color('yellow')
c.pu()
c.right(90)
c.goto(-150,0)
c.down()

c.begin_fill()
for _ in range(2):
    c.fd(300)
    c.left(90)
    c.fd(200)
    c.left(90)

c.end_fill()

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
c.fillcolor('red')

for _ in range(2):
    c.left(90)
    c.fd(200)
    c.left(90)
    c.fd(100)

c.end_fill()

c.pu()
c.goto(-25, 100)
c.color('green')
c.begin_fill()
c.fillcolor('green')
c.down()

c.right(35)

for _ in range(5):
    c.fd(20)
    c.right(72)
    c.fd(20)
    c.left(144)

c.end_fill()
c.left(35)

sleep(5)
c.clear()

# bandeira de cuba

c.pu()
c.goto(-150 , 0)
c.down()

c.color('black')
c.begin_fill()
c.fillcolor('#140778')

for _ in range(2):
    c.fd(300)
    c.left(90)
    c.fd(200)
    c.left(90)
c.end_fill()

c.pu()
c.goto(- 150 , 40)
c.down()

c.begin_fill()
c.fillcolor('white')

for _ in range(2):
    c.fd(300)
    c.left(90)
    c.fd(40)
    c.left(90)
c.end_fill()

c.pu()
c.goto(-150 , 120 )
c.down()

c.begin_fill()
c.fillcolor('white')

for _ in range(2):
    c.fd(300)
    c.left(90)
    c.fd(40)
    c.left(90)
c.end_fill()

c.pu()
c.goto( - 150 , 0)
c.down()
c.color('#ad0707')
c.begin_fill()
c.left(90)

for _ in range(3):
    c.fd(200)
    c.right(120)
c.end_fill()

c.pu()
c.goto( - 120, 110)

c.color('white')
c.begin_fill()

c.right(125)

for _ in range(5):
    c.fd(20)
    c.right(72)
    c.fd(20)
    c.left(144)

c.end_fill()
c.left(35)

sleep(5)
c.clear()

# bandeira da noruega

c.pu()
c.goto(-150 , 0)
c.down()

c.color('red')
c.begin_fill()


for _ in range(2):
    c.fd(300)
    c.left(90)
    c.fd(200)
    c.left(90)
c.end_fill()

c.pu()
c.goto(- 150, 75)
c.down()

c.color('white')
c.begin_fill()

for _ in range(2):
    c.fd(300)
    c.left(90)
    c.fd(50)
    c.left(90)
c.end_fill()

c.pu()
c.goto( -100 , 0)
c.down()

c.begin_fill()
c.left(90)

for _ in range(2):
    c.fd(200)
    c.right(90)
    c.fd(40)
    c.right(90)

c.end_fill()
c.right(90)

c.pu()
c.goto(- 150 , 87.5 )
c.down()

c.color('#09078a')
c.begin_fill()

for _ in range(2):
    c.fd(300)
    c.left(90)
    c.fd(25)
    c.left(90)
c.end_fill()

c.pu()
c.goto(- 90 , 0 )
c.down()

c.begin_fill()
c.left(90)

for _ in range(2):
    c.fd(200)
    c.right(90)
    c.fd(20)
    c.right(90)

c.end_fill()
c.right(90)

c.pu()
c.goto(-150, 0)
c.down()

c.color('black')

for _ in range(2):
    c.fd(300)
    c.left(90)
    c.fd(200)
    c.left(90)

sleep(5)
c.clear()

# bandeira da africa do sul

c.color('black')
c.pu()
c.goto(-150 , 0)
c.down()

for _ in range(2):
    c.fd(300)
    c.left(90)
    c.fd(210)
    c.left(90)

c.pu()
c.goto( - 150, 70)
c.down()

c.color('#1e0a8f')
c.begin_fill()

for _ in range(2):
    c.fd(300)
    c.right(90)
    c.fd(70)
    c.right(90)

c.end_fill()

c.pu()
c.goto(  - 150, 140)
c.down()

c.color('#b01409')
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

c.color('white')
c.begin_fill()

c.left(90)
for _ in range(3):
    c.fd(210)
    c.right(120)

c.end_fill()
c.right(90)

c.pu()
c.goto( - 150, 85)
c.down()

c.color('#1f800b')
c.begin_fill()

for _ in range(2):
    c.fd(300)
    c.left(90)
    c.fd(40)
    c.left(90)
c.end_fill()


c.pu()
c.goto( - 150 ,25)
c.down()

c.color('#1f800b')
c.begin_fill()

c.left(90)
for _ in range(3):
    c.fd(160)
    c.right(120)

c.end_fill()
c.right(90)

c.pu()
c.goto( - 150 ,55)
c.down()

c.color('#e8b62c')
c.begin_fill()

c.left(90)
for _ in range(3):
    c.fd(100)
    c.right(120)

c.end_fill()
c.right(90)

c.pu()
c.goto( - 150 ,70)
c.down()

c.color('black')
c.begin_fill()

c.left(90)
for _ in range(3):
    c.fd(70)
    c.right(120)

c.end_fill()
c.right(90)

c.color('black')
c.pu()
c.goto(-150 , 0)
c.down()

for _ in range(2):
    c.fd(300)
    c.left(90)
    c.fd(210)
    c.left(90)

sleep(5)
c.clear()

# bandeira da republica centro africana

c.pu()
c.goto(-150 , 0)
c.down()

for _ in range(2):
    c.fd(300)
    c.left(90)
    c.fd(200)
    c.left(90)

c.pu()
c.goto( - 150, 50)
c.down()

c.begin_fill()
c.fillcolor('#e8c61e')

for _ in range(2):
    c.fd(300)
    c.right(90)
    c.fd(50)
    c.right(90)

c.end_fill()

c.pu()
c.goto( - 150, 100)
c.down()

c.begin_fill()
c.fillcolor('#369920')

for _ in range(2):
    c.fd(300)
    c.right(90)
    c.fd(50)
    c.right(90)

c.end_fill()

c.pu()
c.goto( - 150, 150)
c.down()

c.begin_fill()
c.fillcolor('#202899')

for _ in range(2):
    c.fd(300)
    c.left(90)
    c.fd(50)
    c.left(90)

c.end_fill()

c.pu()
c.goto( 30, 0)
c.down()

c.color('#b8170b')
c.begin_fill()

for _ in range(2):
    c.left(90)
    c.fd(200)
    c.left(90)
    c.fd(60)

c.end_fill()

c.pu()
c.goto(  - 120 , 180)
c.down()

c.color('#e8c61e')
c.begin_fill()

c.right(35)

for _ in range(5):
    c.fd(15)
    c.right(72)
    c.fd(15)
    c.left(144)

c.end_fill()
c.left(35)




mainloop()