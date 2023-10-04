class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def __str__(self):
        return f'Person(name={self.name}, age={self.age}, email={self.email})'
    

def compare_func(p):
    return p.age

p1 = Person('Alice', 23, 'alice@email.com')
p2 = Person('Bob', 19, 'charlie_brown@email.com')
p3 = Person('Carol', 25, 'carol@email.com')

persons = [p2, p3, p1]
persons2 = sorted(persons, key=compare_func)

#persons.sort(key=compare_func, reverse=True)

for person in persons2:
    print(person)