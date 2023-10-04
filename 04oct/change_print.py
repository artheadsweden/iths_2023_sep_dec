from functools import wraps

def print_with_start(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        pre = ''
        if 'start' in kwargs:
            pre = kwargs['start']
            kwargs.pop('start')
        f(pre, *args, **kwargs)
    return wrapper
    
print = print_with_start(print)


x = 10
print('x is start', x, start='?!?!?!')
print('x is', x, end='')
print('x is', x, end='', sep='-')
print()
print(x, start='>>')
print('done')