grade=[]
gradeInput=int(input("What is the grade for your assignment: "))
grade.append(gradeInput)

while True:
  h= input("Is there anything else that you would like to add to your list enter y/n: ")
  if h== "y" or h=="n":
    print()
    if h=="y":
      z=int(input("Add more items: "))
      grade.append(z)
    elif h=="n":  
      print ("Great, Your average is ")
      break
  else: 
    print("Please enter y or n for Yes or No")

sum=0
for i in grade:
    sum=i+sum
print(sum/len(grade))
    