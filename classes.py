class Person:
    species='Homosapien'

    def hello(self):
        print("hello world")
    
    def __init__(self, name, age) :
        self.name=name
        self.age=age
    
    def hi(self):
        print("Hi my name is "+self.name)


moinul=Person("moinul",45)

print(moinul.name)
print(moinul.age)
print(moinul.species)
moinul.hello()
moinul.hi()


print()

micheal=Person("micheal",17)

print(micheal.name)
print(micheal.age)
print(micheal.species)
micheal.hello()
micheal.hi()

