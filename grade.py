x= input("Whats your GPA: ")
x=int(x)

if x<=59:
    print("Your dumb, you have an f")
elif x>59 and x<=66:
    print("you  have a D")
elif x>67 and x<=79:
    print("you have a C")
elif x>79 and x<=89:
    print("you have a B")
elif x>90 and x<=100:
    print("you have a A")
else:
    print("your not that guy")