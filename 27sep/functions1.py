def func(name):
    print('Hello', name)


def func2(name, age=24):
    print('Hello', name, '! You are', age, 'years old')
    print(f'Hello {name}! You are {age} years old')


def func3(name, names=None):
    if names is None:
        names = []
    names.append(name)
    return names


name_values = ['Pelle']
name_values = func3('Anna')
print(name_values)
name_values = func3('Bosse')
print(name_values)

