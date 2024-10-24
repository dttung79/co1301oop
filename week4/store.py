from product import Product

class Store:
    def __init__(self, name):
        self.name = name        # property name is called
        self.__products = []    # private attribute
    
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
        
    def add_product(self, pid, name, price):
        current_ids = [p.pid for p in self.__products] # create a list of product ids
        # check if the product id already exists
        if pid in current_ids:
            print('Product ID already exists')
            return
        # create a new product object
        p = Product(pid, name, price)
        self.__products.append(p)
        print(f'Product {name} added')

    def get_product(self, pid):
        for p in self.__products:
            if p.pid == pid:
                return p
    
    def edit_product(self, pid, new_name, new_price):
        p = self.get_product(pid)
        if p is None:
            print('Product ID does not exist')
            return
        p.name = new_name
        p.price = new_price
        print(f'Product {pid} updated new name: {new_name}, new price: {new_price}')

    def delete_product(self, pid):
        p = self.get_product(pid)
        if p is None:
            print('Product ID does not exist')
            return
        self.__products.remove(p)   # call the remove method of the list
        print(f'Product {pid} removed')

    def show_products(self):
        print(f'All products in store {self.name}:')
        for p in self.__products:
            print(f'ID {p.pid}: {p.name} - ${p.price}')