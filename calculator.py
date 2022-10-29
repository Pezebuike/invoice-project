
from prettytable import PrettyTable

def FindAmounth(qty: int, price: int) -> int:
    result = qty * price
    return result 

product_table = PrettyTable()
product_table.field_names = ["Product", "Quantity", "Cost Per unit", "Total Amounth"]

while True:
    
    product =input('Enter produt name : ')

    if product == 'q':
        print(' you have finished entering the product: ' )

        break
    else:
        quantity= int(input('Enter product quantity: '))
        price =int(input('Enter price of the item: '))
        amounth = FindAmounth( quantity ,price)
        print(amounth)
        product_table.add_row([product,quantity, price, amounth])
        continue



print(product_table)

