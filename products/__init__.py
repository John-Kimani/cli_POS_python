from dashboard import dashboard
from .product import ProductProfile
products_database = 'database/products.json'       

def create_product():
    '''
    Create new product
    '''
    print('********************')
    print('Enter requested details to create new product into the system')
    product_name = input('''Enter name of the new product: ''')
    quantity = int(input('''Enter quantity received: '''))
    price = float(input('''Enter price: '''))
    description = input('''Tell about the product: ''')
    try: 
        print('Creating product...')
        ProductProfile.save_product(product_name, quantity, price, description)
    except:
        print("Something went wrong")


def display_all_products():
    '''
    Show all products
    '''
    print('*****************************')
    print('List of available products')
    print('*****************************')
    ProductProfile.display_all_products()


def search_product_by_name():
    '''
    Filter product by name
    '''
    product_name = input('Enter product name: ')
    product = ProductProfile.product_exist(product_name)
    if product == True:
        print("***************")
        print("Item found")
        print("***************")
        ProductProfile.search_product_by_name(product_name)
    elif product == False:
        print("Please view all the available products.")
    else:
        print("An error occured. Please contact Admin")

def search_product_by_id():
    '''
    Filter products by ID
    '''
    product_id = input('Enter product ID: ')
    found = ProductProfile.product_exist_by_id(product_id)
    if found == True:
        product = ProductProfile.search_product_by_id(product_id=product_id)
        print('**************')
        print('Product Found')
        print('**************')
        print(product)
        print('**************')
    elif found == False:
        print('**************')
        print('Product with such ID does not exist')
        print('**************')

def update_product():
    '''
    Update product instance
    '''
    product_id = input('Enter ID: ')
    product = ProductProfile.product_exist_by_id(product_id)
    if product == True:
        product_name = input('Enter new name: ')
        quantity = int(input('''Enter quantity received: '''))
        price = float(input('''Enter price: '''))
        description = input('''Tell about the product: ''')
        ProductProfile.update_product(product_id=product_id, product_name = product_name, quantity = quantity, price = price, description = description)
    elif product == False:
        print('Product with that ID does not exist!')
        print("!!!!!!!!!!!!!!!!!!!!!!!")
        print("Please try again...")
        update_product()
    else:
        print("An error occured. Please contact Admin")


def delete_product():
    product_name = input('Enter product name: ')
    product_to_delete = ProductProfile.product_exist(product_name)
    if product_to_delete == True:
        ProductProfile.search_product_by_name(product_name)
        print('Are you sure you want to delete ' + product_name)
        print('This information will forever be lost!!!')
        product_id = input("Enter product ID: ")
        danger = 0
        while True:
            danger = input('Type 1 to confirm action or 00 to go back!')
            if danger == "1":
                ProductProfile.delete_product(product_id)
                print(f"{product_name}'s Account has been deleted!")
            elif danger == "00":
                delete_product()
            break
    elif product_to_delete == False:
        print("Product does not exist")
