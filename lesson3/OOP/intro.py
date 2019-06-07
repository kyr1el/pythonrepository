class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def coordinates(self):
        print(f'Координаты: x={self.x},y={self.y}')
    def __repr__(self):
        return f'<point x = {self.x}, y = {self.y}>'
my_point = point(12,1)
print(my_point)
