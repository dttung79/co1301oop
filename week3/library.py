# syntax to import a class from another file
# from filename import classname
from book import Book

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        # check if book id already exists
        if self.check_id(book.bid):
            print(f'Book {book.bid} already exists!')
            return
        # new book, add to the list
        self.books.append(book)
        print(f'Book {book.bid} added successfully!')
    
    def check_id(self, bid):
        for b in self.books:
            if b.bid == bid:
                return b
        return None
    
    def delete_book(self, bid):
        del_book = self.check_id(bid)
        if del_book == None:
            print(f'Book {bid} not found!')
            return
        
        self.books.remove(del_book)
        print(f'Book {bid} deleted successfully!')

    
    def edit_book(self, bid, new_name, new_price):
        edit_book = self.check_id(bid)
        if edit_book == None:
            print(f'Book {bid} not found!')
            return
        
        edit_book.name = new_name
        edit_book.price = new_price
        print(f'Book {bid} edited successfully!')

    def borrow_book(self, bid):
        # check id exist
        borrow_book = self.check_id(bid)
        if borrow_book == None:
            print(f'Book {bid} not found!')
            return
        # check borrow status
        if borrow_book.borrowed:
            print(f'Book {bid} already borrowed!')
            return
        # update borrow status
        borrow_book.borrowed = True
        print(f'Book {bid} borrowed successfully!')
    
    def return_book(self, bid):
        # check id exist
        return_book = self.check_id(bid)
        if return_book == None:
            print(f'Book {bid} not found!')
            return
        # check borrow status
        if not return_book.borrowed:
            print(f'Book {bid} has not borrowed!')
            return
        # update borrow status
        return_book.borrowed = False
        print(f'Book {bid} returned successfully!')
    
    def show_books(self):
        print('Books in the library: ')
        for b in self.books:
            b.show()
            print('----------------------')

### Test library
if __name__ == '__main__':
    lib = Library()
    lib.add_book(Book(1, 'Python Programming', 25))
    lib.add_book(Book(2, 'Java Programming', 30))
    lib.add_book(Book(3, 'C Programming', 20))
    lib.show_books()

    # add a book with existing id
    lib.add_book(Book(2, 'C++ Programming', 20))

    # delete a book with id not found
    lib.delete_book(5)

    # delete a book with id found
    lib.delete_book(2)
    lib.show_books()

    # edit a book with id found
    lib.edit_book(1, 'Python Programming', 30)

    # borrow a book
    lib.borrow_book(1)
    lib.show_books()
    # return a book
    lib.return_book(1)
    lib.show_books()