books = {1: ['Dragonball', 400, False], 2: ['Naruto', 200, False], 3: ['One Piece', 800, True], 4: ['Death Note', 100, False]}

def book_manage():
    # Display the menu with options: add book, delete book, display books, change price, borrow book, return book, exit
    running = True
    while running:
        print_menu()
        choice = int(input('Enter your choice: '))
        if      choice == 1:    add_book()
        elif    choice == 2:    delete_book()
        elif    choice == 3:    display_books()
        elif    choice == 4:    change_price()
        elif    choice == 5:    borrow_book()
        elif    choice == 6:    return_book()
        elif    choice == 0:    running = False
        else:                   print('Invalid option!')
    print('Program ends.')

def print_menu():
    print('Book Management')
    print('1. Add book')
    print('2. Delete book')
    print('3. Display books')
    print('4. Change price')
    print('5. Borrow book')
    print('6. Return book')
    print('0. Exit')

def add_book():
    new_id = int(input('Enter book ID: '))
    # validate new_id to make sure it is not already in the dictionary books
    if new_id in books:
        print('Book ID already exists!')
        return
    # enter other details of the new book
    new_name = input('Enter book name: ')
    new_price = int(input('Enter book price: '))
    # Add the new book to the dictionary books, borrowing status is False by default
    books[new_id] = [new_name, new_price, False]

    print('Book added successfully!')

def delete_book():
    del_id = int(input('Enter book ID to delete: '))
    
    if del_id not in books:
        print(f'Book ID {del_id} not found!')
        return
    
    del books[del_id]
    print('Book deleted successfully!')

def display_books():
    for book_id, book_info in books.items():
        print(f'Book ID: {book_id}')
        print(f'Book name: {book_info[0]}')
        print(f'Price: ${book_info[1]}')
        print(f'Borrowed: {book_info[2]}')
        print()

def change_price():
    change_id = int(input('Enter id to change: '))

    if change_id not in books:
        print(f'Book ID {change_id} not found!')
        return
    
    new_price = int(input('Enter new price: '))
    # change price of the book with id change_id
    books[change_id][1] = new_price # 1 is the index of price in the list of book info

    print('Price changed successfully!')

def borrow_book():
    change_id = int(input('Enter id to borrow: '))

    if change_id not in books:
        print(f'Book ID {change_id} not found!')
        return
    
    if books[change_id][2] == True:
        print('Book already borrowed!')
        return
    
    # change borrow status of the book with id change_id
    books[change_id][2] = True # 2 is the index of borrow status in the list of book info

def return_book():
    change_id = int(input('Enter id to return: '))

    if change_id not in books:
        print(f'Book ID {change_id} not found!')
        return
    
    if books[change_id][2] == False:
        print('Book not borrowed!')
        return
    
    # change borrow status of the book with id change_id
    books[change_id][2] = False # 2 is the index of borrow status in the list of book info


# Call the function book_manage() to start the program
book_manage()