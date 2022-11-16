def helloWorld():
    print("hello world")
helloWorld()

print()
print("Add")
print()

#This function adds the two values that are in the end statement 
def add(a,b):
    print(a+b)

add(9,10)

print()
print("Subtract")
print()

#This function subtracts the two values
def subtract(a,b):
    print(a-b)

subtract(9,10)

print()
print("multiply")
print()

#This value multiplies 
def multiply(a,b):
    print(a*b)

multiply(9,10)

print()
print("divide")
print()

#This function divides
def divide(a,b):
    print(a/b)

divide(9,10)

print()
print("modular")
print()


#This functions uses modular which divides the value and give the remainder
def remainder(a,b):
    print(a%b)

remainder(9,10)

print()

print()
print("return value")
print()

def returnValue(a,b):
    return a+b

x= returnValue(9,10)

print(x)

print()

def slope(m,x,b):
    return m*x+b

y=slope(5,5,5)

print(y)