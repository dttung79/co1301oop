class Book:
    def __init__(self, bid, name, price):
        self.bid = bid
        self.name = name
        self.price = price
        self.borrowed = False

    def show(self):
        available = 'not available' if self.borrowed else 'available'
        print(f'{self.bid}: {self.name}, ${self.price}, {available}')


### Test some objects
if __name__ == '__main__':
    b1 = Book(1, 'Python Programming', 25)
    b2 = Book(2, 'Java Programming', 30)
    b3 = Book(3, 'C Programming', 20)
    b3.borrowed = True

    b1.show()
    b2.show()
    b3.show()