#Jaspar 19.11.24
#ÜL13

import turtle
 
screen = turtle.Screen()
t = turtle.Turtle()
 

import turtle
turtle.speed(0)
screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)

cm = 10
mm= 3
# Küsi kasutajalt numbrilist sisendit
pikkus = screen.numinput("Vanuse sisestamine", "Mis on sinu joonlaua pikkus?", default=20, minval=0, maxval=100)
pikkus = 8

for i in range(pikkus):
    for j in range(10):

        t.fd(mm)
        t.lt(90)
        t.fd(mm)
        t.lt(180)
        t.fd(mm)
        t.lt(90)
    t.lt(90)
    t.fd(cm)
    t.write(i+1,font=("Arial", 8, "normal"))
    t.lt(180)
    t.fd(cm)
    t.lt(90)
turtle.done()
