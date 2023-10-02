class Person:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def __str__(self):
        return f'{self.name} is {self.age} years old and has email {self.email}'

p1 = Person('Alice', 'alice@email.com', 34)
p2 = Person('Bob', 'bob@email.com', 44)

print(p1.__dict__)
print(p2.__dict__)
