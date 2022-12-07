
try:
    age = int(input('Enter your age: '))

    faveNum = int(input('What is your favorite number: '))

    if age <= 21:
        print('You are not allowed to enter, you are too young.')
    else:
        print('Welcome, you are old enough.')
        
    print("Fun Fact! Your age divided by your favorite number is: " , age / faveNum)

except ValueError:
    print("Please Input a Number ")
except ZeroDivisionError:
    print("please enter values such as Zero")

finally:
    print("running no matta wat boi")
