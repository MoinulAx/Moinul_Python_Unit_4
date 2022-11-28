from turtle import *

speed(0)

penup()
setposition(0,-50)
pendown()
begin_fill()
color("yellow")
circle(200)
end_fill()

def eye():
    begin_fill()
    color("white")
    circle(50)
    end_fill()

def pupil():
    begin_fill()
    color("black")
    circle(25)
    end_fill()




penup()
setposition(-80,50)
pendown()

pensize(5)
color("black")
right(90)
circle(80,180)

penup()
setposition(120,200)
pendown()

eye()

penup()
setposition(-20,200)
pendown()

eye()

penup()
setposition(120,200)
pendown()

pupil()

penup()

setposition(-60,200)
pendown()

pupil()













input()