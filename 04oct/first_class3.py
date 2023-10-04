import time
from functools import wraps

def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Took {end - start} seconds')
        return result
    return wrapper

@time_it
def my_func(x):
    # Simulate long running task
    x += 1
    time.sleep(2)
    return x

@time_it
def my_func2(x, y, z, name='Adder'):
    print(f'In function {name}')
    time.sleep(3)
    return x + y + z

# my_func = time_it(my_func)
# print(my_func.__name__)
print(my_func2(2, 3, 4, name='Plussaren'))

