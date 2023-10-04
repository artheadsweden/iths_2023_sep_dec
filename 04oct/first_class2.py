def func_factory(power):
    def power_func(number):
        return number**power
    return power_func


square = func_factory(2)
print(square(3))
cube = func_factory(3)
print(cube(3))
print(square(4))
print(cube(99))