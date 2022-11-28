from random import randint,choice as randchoice
from turtle import *

# penup()
# setposition(-300,0)
# pendown()
colors=["red","blue","purple","green","cyan","yellow","orange","pink","brown"]
speed(0)
for i in range(150):
   
    penup()
    setposition(randint(-200,200),randint(-200,200))
    pendown()

    pencolor(randchoice(colors))
    pensize(randint(4,8))
    
    begin_fill()
    fillcolor(randchoice(colors))
    circle(randint(10,50), steps=randint(3,15))
    right(randint(1,360))
    end_fill()

    # forward(randint(1,100))
done()