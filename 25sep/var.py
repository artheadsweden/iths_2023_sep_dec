# Integer
i = 1
print(i)
# Float
f = 10.2
print(f)
# String
s = 'hej'
print(s.title())

# Boolean
done = False

# List
values = [1, 2, 3]
print(id(values))
values.remove(2)
print(id(values))

print(values[1])

# Tuple
values2 = (1, 2, 3)
print(type(values2))

# Set
values3 = {1, 2, 3, 2, 3, 4, 2}
print(values3)

# Dictionary
values4 = {
    'name': 'Alice',
    'age': 34,
    'email': 'alice@email.com'
}

print(values4['email'])