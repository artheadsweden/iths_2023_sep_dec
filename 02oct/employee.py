class Employee:
    increase = 1.04

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def __str__(self):
        return f'{self.first_name}, {self.last_name} earns {self.salary}'
    
    def increase_salary(self):
        self.salary = int(self.salary * self.increase)
    
class Developer(Employee):
    increase = 1.10

    def __init__(self, first_name, last_name, salary, prog_lang):
        super().__init__(first_name, last_name, salary)
        self.prog_lang = prog_lang

    def __str__(self):
        return f'{super().__str__()} and fav prog lang is {self.prog_lang}'
    
class Boss(Employee):
    increase = 1.05

emp1 = Employee('Alice', 'Ason', 45000)
emp2 = Employee('Bob', 'Bson', 42000)
dev1 = Developer('Carl', 'Cson', 50000, 'Python')
boss1 = Boss('Dana', 'Dson', 50000)

print(emp1)
print(emp2)
print(dev1)
print(boss1)

emp1.increase_salary()
emp2.increase_salary()
dev1.increase_salary()
boss1.increase_salary()

print(emp1)
print(emp2)
print(dev1)
print(boss1)

if isinstance(dev1, Boss):
    print('Is Boss')
else:
    print('Is not Boss')
