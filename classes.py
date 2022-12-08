class Person:
    species='Homosapien'

    def hello(self):
        print("hello world")
    
    def __init__(self, name, age) :
        self.name=name
        self.age=age
    
    def hi(self):
        print("Hi my name is "+self.name)

class Teacher(Person):
    role='teacher'
    
    def hi(self):
        print("Hi my name is Mx."+self.name)

class Student(Person):
    role="students"

moinul=Student("moinul",45)

print(moinul.name)
print(moinul.age)
print(moinul.species)
moinul.hello()
moinul.hi()
print(moinul.role)


print()

micheal=Person("micheal",17)

print(micheal.name)
print(micheal.age)
print(micheal.species)
micheal.hello()
micheal.hi()

print()

forlenza= Teacher('forlenza',184)
print(forlenza.role)
forlenza.hi()