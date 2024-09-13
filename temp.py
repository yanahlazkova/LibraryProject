class Person:
    name= "Alex"
    def __init__(self, age: int):
        self.age = age

    @classmethod
    def change_name(cls, new_name):
        cls.name = new_name


obj1 = Person(25)
obj2 = Person(35)
obj2.name = "obj2"
print(Person.mro())
print(Person.name)
print(obj2.name)
print(obj1.name)
obj2.change_name("obj3")
print(obj2.name)
print(obj1.name)

