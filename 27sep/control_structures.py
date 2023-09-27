# For-loops


for i in range(10):
    if i == 5:
        continue
    print(i)
    if i == 7:
        break
else:
    print('In else')

print('Done')

values = [1, 2, 3, 'Anna', True]

for i, value in enumerate(values):
    print('hej', i, value)

for i in range(len(values)):
    print('hej', i, values[i])

# Use range to create a list

values = list(range(2, 100, 4))

print(values)

# if-statement
x = 10
y = 20

if x > 10 or y == 20:
    print('Bigger than 10')
else:
    print('Less or equal to 10')

grade = 25

if grade < 10:
    print('bad')
elif grade < 20:
    print('ok')
elif grade < 30:
    print('good')

# While-loop

x = 10

while x < 44:
    print(x)
    x *= 2
