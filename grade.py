#the variable that hold the input being the grade for this instance.
x= input("Whats your GPA: ")

#converts the variable from a string to a float so the numeric value can be checked. All input values are strings unless they are converted.
x=float(x)

#the if statement is a loop looking for 
if x<=59:
    print("Your dumb, you have an f")
elif x>59 and x<=69:
    print("you  have a D")
elif x>69 and x<=79:
    print("you have a C")
elif x>79 and x<=89:
    print("you have a B")
elif x>89 and x<=100:
    print("you have a A")
else:
    print("your not that guy")