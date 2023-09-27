def my_range1(n):
    i = 0
    values = []
    while i < n:
        values.append(i)
        i += 1
    return values


def my_range2(n):
    print('Start')
    i = 0
    while i < n:
        yield i
        i += 1

values = [1, 2, 3, 4]

my_range3 = (value**2 for value in values)

for i, value in enumerate(my_range3):
    print(value)
    if i >= 1:
        break

print('Hepp')
for i, value in enumerate(my_range3):
    print(value)
    if i > 1:
        break