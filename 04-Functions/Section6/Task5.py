class range:
    def __init__(self, x, y):
        if x > y:
            self.x =  y
            self.y = x
        else:
            self.x =  x
            self.y = y
    def __str__(self):
        return f'<{self.x}, {self.y}>'
    def contains(self, value):
        if(value >= self.x and value <= self.y):
            return True
        else:
            return False

r1 = range(2, 15)

print('Number 7 in the range <2, 15>: ', r1.contains(7))