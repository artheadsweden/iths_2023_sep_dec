def func(*args):
    print(args)


def func2(a, b, **kwargs):
    print(a, b)
    if 'c' in kwargs:
        print(kwargs['c'])
    if 'd' in kwargs:
        print(kwargs['d'])
    print(kwargs)


def func3(a, b, *args, name='John', **kwargs):
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'args = {args}')
    print(f'name = {name}')
    print(f'kwargs = {kwargs}')


func()
func(1)
func(1, 2)
func(1, 2, 3)

func2(1, 2, c=14, d=33)

func3(1, 2, 3, 4, 5, name='Anna', age=34, email='anna@email.com')