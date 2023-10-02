class Person:
    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person({self.name}, {self.age})'
    

p1 = Person('Alice', 34)
p2 = Person('Bob', 45)

print(p1)
print(p2)
# p1.email = 'alice@email.com'
print(p1.email)