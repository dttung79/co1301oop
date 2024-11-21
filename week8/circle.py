from shape import Shape

class Circle(Shape):
    PI = 3.14
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Radius must be a number")
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    # override the area property to calculate the area of a circle
    @property
    def area(self):
        return Circle.PI * self.radius ** 2
    
    # override the __str__ method to add the radius of the circle
    def __str__(self) -> str:
        return super().__str__() + f', radius: {self.radius}'
    
if __name__ == "__main__":
    c1 = Circle("Circle O", 5)
    print(c1)   # here __str__ method is called
    c2 = Circle("Circle P", 10)
    print(c2)