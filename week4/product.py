class Product:
    def __init__(self, pid, name, price):
        self.__pid = pid    # private attribute
        self.name = name    # public setter
        self.price = price  # public setter
    
    @property
    def pid(self):
        return self.__pid
    
    # no setter for pid

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if value == '':
            print('Name cannot be empty')
            self.__name = 'No name'
        else:
            self.__name = value

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value < 0:
            print('Price cannot be negative')
            self.__price = 0
        else:
            self.__price = value