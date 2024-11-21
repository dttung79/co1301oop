from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, name, side):
        super().__init__(name, side, side)

    @property
    def side(self):
        return self.width
    
    @side.setter
    def side(self, value):
        self.width = value
        self.height = value

if __name__ == "__main__":
    s1 = Square("Square ABCD", 5)
    print(s1)
    s1.side = 10
    print(s1)