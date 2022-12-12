from turtle import Turtle, Screen
from random import randint,choice as randchoice

colors=["red","blue","purple","green","cyan","yellow","orange","pink","brown"]

class MyTurtle(Turtle):
    def random_shape(self,x,y):
        super().__init__()
        self.color(randchoice(colors))
    
    
        self.penup()
        self.setposition(randint(-200,200),randint(-200,200))
        self.pendown()

        self.circle(randint(10,150), steps=randint(3,15))
        # self.right(randint(1,360))

    def __init__(self) -> None:
        super().__init__()
        self.random_shape(0,0)
        self.onclick(self.random_shape)

        

x=MyTurtle()
y=MyTurtle()

x.forward(50)
y.backward(50)

screen=Screen()

screen.mainloop()
