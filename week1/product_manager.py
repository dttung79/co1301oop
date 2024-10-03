# declare 3 lists for products' information
ids = [1, 2, 3, 4, 5]
names = ['iphone', 'samsung', 'xiaomi', 'huawei', 'oppo']
prices = [600, 500, 400, 300, 200]

def main():
    running = True
    while running:
        print_menu()
        choice = int(input('Enter your choice: '))
        if choice == 1:
            list_products()
        elif choice == 2:
            search_id()
        elif choice == 3:
            most_expensive()
        elif choice == 4:
            sort_prices()
        elif choice == 5:
            add_product()
        elif choice == 6:
            lowest_price()
        elif choice == 7:
            sort_desc()
        elif choice == 8:
            search_name()
        elif choice == 0:
            running = False
        else:
            print('Invalid option!')
    print('Program ends.')

def print_menu():
    print('Product Management')
    print('1. List products')
    print('2. Search by ID')
    print('3. Most expensive')
    print('4. Sort by price')
    print('5. Add product')
    print('6. Find lowest price')
    print('7. Sort by price descendant')
    print('8. Search by name')
    print('0. Exit')

def list_products():
    n = len(ids) # get number of items in list ids
    for i in range(n):
        print(f'ID: {ids[i]}, Name: {names[i]}, Price: ${prices[i]}')
    print()

def search_id():
    pid = int(input('Enter ID to search: '))
    n = len(ids)
    found = False
    for i in range(n):
        if ids[i] == pid: # found id
            print(f'ID: {ids[i]}, Name: {names[i]}, Price: ${prices[i]}')
            found = True
            break   # no need to continue searching
    if not found:
        print(f'No product found for id {pid}!')

def search_name():
    name = input('Enter name to search: ')
    n = len(ids)
    found = False
    for i in range(n):
        if name in names[i]: # found name (approximately)
            print(f'ID: {ids[i]}, Name: {names[i]}, Price: ${prices[i]}')
            found = True
    if not found:
        print(f'No product found for name {name}!')

def most_expensive():
    max_price = prices[0] # set max price at position 0
    max_pos = 0

    for i in range(1, len(prices)):
        if prices[i] > max_price: # if price at i-position > current max price
            max_price = prices[i] # update max price
            max_pos = i           # update the new max position

    print('Most expensive product: ')
    print(f'ID: {ids[max_pos]}, Name: {names[max_pos]}, Price: ${prices[max_pos]}')

def lowest_price():
    min_price = prices[0] # set min price at position 0
    min_pos = 0

    for i in range(1, len(prices)):
        if prices[i] < min_price: # if price at i-position > current min price
            min_price = prices[i] # update min price
            min_pos = i           # update the new min position

    print('Lowest price product: ')
    print(f'ID: {ids[min_pos]}, Name: {names[min_pos]}, Price: ${prices[min_pos]}')

def sort_prices():
    for i in range(len(ids) - 1):
        for j in range(i + 1, len(ids)):
            if prices[j] < prices[i]: # price at j-pos less than price at i-pos
                ids[i], ids[j] = ids[j], ids[i]
                names[i], names[j] = names[j], names[i]
                prices[i], prices[j] = prices[j], prices[i]
    print('Sort by prices: ')
    list_products()

def sort_desc():
    for i in range(len(ids) - 1):
        for j in range(i + 1, len(ids)):
            if prices[j] > prices[i]: # price at j-pos greater than price at i-pos
                ids[i], ids[j] = ids[j], ids[i]
                names[i], names[j] = names[j], names[i]
                prices[i], prices[j] = prices[j], prices[i]
    print('Sort by prices: ')
    list_products()

def add_product():
    pid = int(input('Enter new product id: '))
    name = input('Enter new product name: ')
    price = int(input('Enter new product price: '))

    ids.append(pid)
    names.append(name)
    prices.append(price)

    print('New product added.')

### Main program ###
main()
