def func(value):
    return value, value*2, value*3, value*4


a, *b, c = func(10)
print(a)
print(b)
print(c)

# t = (7, 2, 5, 8, 1)

# first, *_, last = t
# print(first)
# print(last)
