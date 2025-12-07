class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name, self.age)

class Emplyee(Person):
    def _init__(self, name, age, empid):
        super().__init__(name, age)

a=Emplyee("riya", 25, 1001)
a.display()


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init(fname, lname)
        self. graduationyear = year
x=Student("Mike", "Tyson", 2025)
x.printname()
print(x.graduationyear)



class Parrot:
    species={"bird"}
    def __init__(self, name, age):
        self.name = name
        self.age = age
blue=Parrot("blue", 10)
woo=Parrot("woo", 15)
print("blue is a {}".format(blue.__class__.species))
print("woo is also{}".format(woo.__class__.species))
