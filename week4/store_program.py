from product import Product
from store import Store

class StoreProgram:
    def __init__(self):
        name = input('Enter store name: ')
        self.__store = Store(name)    

    def run(self):
        running = True
        while running:
            self.__print_menu()
            choice = int(input('Enter choice: '))
            if choice == 1:     self.__add_product()
            elif choice == 2:   self.__edit_product()
            elif choice == 3:   self.__delete_product()
            elif choice == 4:   self.__show_products()
            elif choice == 5:   running = False
            else:               print('Invalid choice')
    
    def __print_menu(self):
        print('1. Add product')
        print('2. Edit product')
        print('3. Delete product')
        print('4. Show products')
        print('5. Exit')
    
    def __add_product(self):
        pid = int(input('Enter product ID: '))
        name = input('Enter product name: ')
        price = float(input('Enter product price: '))
        self.__store.add_product(pid, name, price)

    def __edit_product(self):
        pid = int(input('Enter product ID: '))
        name = input('Enter new product name: ')
        price = float(input('Enter new product price: '))
        self.__store.edit_product(pid, name, price)
    
    def __delete_product(self):
        pid = int(input('Enter product ID: '))
        self.__store.delete_product(pid)
    
    def __show_products(self):
        self.__store.show_products()

if __name__ == '__main__':
    program = StoreProgram()
    program.run()