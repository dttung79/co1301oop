from shape import Shape

class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Width must be a number")
        if value <= 0:
            raise ValueError("Width must be positive")
        self._width = value

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Height must be a number")
        if value <= 0:
            raise ValueError("Height must be positive")
        self._height = value

    @property
    def area(self):
        return self.width * self.height
    
    def __str__(self) -> str:
        return super().__str__() + f', dimensions: {self.width} x {self.height}'

if __name__ == "__main__":
    r1 = Rectangle("ABCD", 5, 10)
    print(r1)