from circle import Circle
from rectangle import Rectangle
from square import Square

if __name__ == "__main__":
    o1 = Circle("Circle O", 5)
    r1 = Rectangle("Rectangle ABCD", 5, 10)
    s1 = Square("Square XYZ", 5)

    shapes = [o1, r1, s1]
    # polymorphism is used here to call the __str__ method of each shape
    # in turn, __str__ calls corresponding area property of each shape
    for s in shapes:
        print(s)