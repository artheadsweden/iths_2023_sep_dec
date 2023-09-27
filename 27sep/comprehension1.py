values = [1, 2, 3, 4]

new_values = []

for value in values:
    if value % 2 == 0:
        new_values.append(value**2)
    else:
        new_values.append(value)

print(new_values)

# Comprehension
new_values = [value**2 for value in values]
print(new_values)

x = 10

y = 'a' if x <= 10 else 'b'
print(y)