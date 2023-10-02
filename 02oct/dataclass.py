from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

    def swap_xy(self):
        self.x, self.y = self.y, self.x


p1 = Point(10, 20)
p2 = Point(20, 40)

print(p1)
print(p2)

p1.swap_xy()
print(p1)