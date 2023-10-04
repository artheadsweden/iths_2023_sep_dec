def func(x):
    return x - 1

def func2(x):
    return x + 1

def func3(the_character):
    return the_character.upper()


def mapper(helper_func, iterable):
    result = []
    for value in iterable:
        helper_result = helper_func(value)
        result.append(helper_result)
    return result

values = [1, 2, 3, 4, 5]
result = map(lambda x: x + 1, values)

print(list(result))

name = 'joakim'
name2 = ''.join(mapper(func3, name))
print(name2)

