a=input("Seprate each grade with a comma To receive average ")

grade=a.split(",")

a=int(a)



total=sum(grade)

print ("Your average is"+str(total/len(grade)))


