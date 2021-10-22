class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)

my_square = Square(10)
print(my_square.width)
print(my_square.height)


