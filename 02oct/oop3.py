class Person:
    def __init__(self, **kwrags):
        self.__dict__ = kwrags

    def __str__(self):
        return f'{self.name} is {self.age} years old'

p1 = Person(name='Alice', age = 23)
p2 = Person(name='Bob', age=33)
print(p1)
print(p2)