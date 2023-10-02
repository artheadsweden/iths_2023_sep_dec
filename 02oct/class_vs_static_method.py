class SomeClass:
    def __init__(self, value):
        self.value = value

    def inc_value(self):
        self.value += 1

    @staticmethod
    def static_mthd():
        print('Static method')

    @classmethod
    def class_mthd(cls):
        print(f'Class Method in {cls}')
        return cls(100)

s1 = SomeClass(10)
print(s1.value)
s1.inc_value()
print(s1.value)
SomeClass.static_mthd()
s2 = SomeClass.class_mthd()
print(s2.value)


