import time
from functools import wraps

def repeat(n, delay):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
                time.sleep(delay)
            return result
        return wrapper
    return decorator


@repeat(3, 2)
def say_hi(name):
    print('Inside say_hi')
    return f'Hi {name}'


def greet(greeting, name):
    return f'{greeting}! {name}.'


print(say_hi('Anna'))
print(greet('Yo', 'Bob'))