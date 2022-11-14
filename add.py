#This is the variable that hold the first input value that the user would have input. The string in the parentheses describing the type of information that the user would input.
a=input("whats the first number: ")

#This is the variable that hold the second input value that the user would have input. The string in the parentheses describing the type of information that the user would input.
b=input ("whats your second number: ")

#The line comes before the result to state the value done  by the operations on the new line adn thst it has to be first due to python be a interpeter language.
print("Your result is")

#this is where the vakues that have been inputed become converted and combined. Its converted from a string to a float so numbers with decimal can be added.
print (float(a) + float (b))