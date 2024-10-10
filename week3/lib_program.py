from book import Book
from library import Library

class LibraryProgram:
    def __init__(self):
        self.lib = Library() # create a library object
    
    def run(self):
        running = True
        while running:
            self.print_menu()
            choice = int(input('Enter your choice: '))
            if choice == 1: self.add_book()
            elif choice == 2: self.edit_book()
            elif choice == 3: self.delete_book()
            elif choice == 4: self.borrow_book()
            elif choice == 5: self.return_book()
            elif choice == 6: self.list_all()
            elif choice == 0: running = False
            else: print('Invalid choice')
    
    def print_menu(self):
        print('1. Add new book')
        print('2. Edit a book')
        print('3. Delete a book')
        print('4. Borrow a book')
        print('5. Return a book')
        print('6. Show all books in library')
    
    def add_book(self):
        # Ask user to enter book information
        bid = int(input('Enter book id: '))
        name = input('Enter book name: ')
        price = int(input('Enter book price: '))
        # create a book object
        new_book = Book(bid, name, price)
        # call method of library to add new book
        self.lib.add_book(new_book)

    def edit_book(self):
        # Ask user to enter book information
        bid = int(input('Enter book id: '))
        name = input('Enter book name: ')
        price = int(input('Enter book price: '))

        self.lib.edit_book(bid, name, price)
    
    def delete_book(self):
        bid = int(input('Enter book id: '))
        self.lib.delete_book(bid)

    def borrow_book(self):
        bid = int(input('Enter book id: '))
        self.lib.borrow_book(bid)
    
    def return_book(self):
        bid = int(input('Enter book id: '))
        self.lib.return_book(bid)

    def list_all(self):
        self.lib.show_books()

if __name__ == '__main__':
    program = LibraryProgram()
    program.run()