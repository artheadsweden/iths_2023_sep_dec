values = [1, 2, 3, 4]
# List Comprehension
new_values = [value**2 for value in values]
print(type(new_values))

# Set Comprehension
new_values = {value**2 for value in values}
print(type(new_values))

# Dict Comprehension
new_values = {value: value**2 for value in values}
print(type(new_values))
print(new_values)

# Tuple Comprehension
new_values = tuple([value**2 for value in values])
print(type(new_values))
