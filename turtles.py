from turtle import *

# while  True:

# forward(20)

# penup()
# backward(200)
# pendown()
# forward(100)

# penup()
# forward(100)
# pendown()
# forward(100)
# penup()
# forward(100)
# pendown()
# penup()
# forward(100)
# pendown()
# forward(100)
# penup()
# forward(100)
# pendown()


penup()
backward(250)
pendown()

user_int = int(input("Enter an integer: "))
for i in range(1, user_int):    
    forward(50)
    penup()
    forward(50)
    pendown()

input()

