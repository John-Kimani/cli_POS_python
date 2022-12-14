def dashboard ():
    '''
    Menu function
    '''
    options = 0


    while options != "0":
        print("** User dashboard **")
        options = input(''' 
        1. Products
        2. Customers
        3. Purchases
        0. Close app
        
        From the list above select an option to continue: 
        ''')

        if options == "1":
            while True:
                print("Products section")
                select_task = input('''
                1. Create product 
                2. View product list
                3. Search product by name
                4. Search product by ID
                5. Update product infomation
                6. Delete product 
                00. Back to dashboard 
                ''')

                if select_task == "1":
                    from products import create_product
                    create_product()
                elif select_task == "2":
                    from products import display_all_products
                    display_all_products()
                elif select_task == "3":
                    from products import search_product_by_name
                    search_product_by_name()
                elif select_task == "4":
                    from products import search_product_by_id
                    search_product_by_id()
                elif select_task == "5":
                    from products import update_product
                    update_product()
                elif select_task == "6":
                    from products import delete_product
                    delete_product()
                elif select_task == "00":
                    print('Taking you back to the dashboard')
                    dashboard()
                else:
                    print('Warning!: Invalid input')
                    print('Please check choices provided then try again.')

        elif options == "2":
            while True:
                print("Customer Section")
                select_task = input('''
                1. Create new customer account 
                2. View all customers
                3. Find cutomer account by ID
                4. Find customer by name
                5. Update customer account 
                6. Delete customer account
                00. Back to dashboard 
                ''')

                if select_task == "1":
                    from customers import create_customer
                    create_customer()
                elif select_task == "2":
                    from customers import display_all_customer_accounts
                    display_all_customer_accounts()
                elif select_task == "3":
                    from customers import search_customer_by_id
                    search_customer_by_id()
                elif select_task == "4":
                    from customers import search_customer_by_name
                    search_customer_by_name()
                elif select_task == "5":
                    from customers import update_customer_account
                    update_customer_account()
                elif select_task == "6":
                    from customers import delete_customer_account
                    delete_customer_account()

                elif select_task == "00":
                    print('Taking you back to the dashboard')
                    dashboard()
                else:
                    print('Warning!: Invalid input')
                    print('Please check choices provided then try again.')
        elif options == '3':
            while True:
                print("Purchases section")
                select_task = input('''
                1. Buy Item(s)
                2. View History
                00. Go back to Dashboard
                ''')
                if select_task == '1':
                    from purchases import purchase_items
                    purchase_items()
                elif select_task == '2':
                    print('W.I.P')
                elif select_task == '00':
                    print("#############")
                    print('Back to Dashboard.')
                    dashboard()
                else:
                    print('Warning!: Invalid input')
                    print('Please check choices provided then try again.')
        
        elif options == "0":
            print("Application is closing")
            print("Thank you. See you soon!")
        else:
            print('Warning!!!')
            print('Invalid input')
            print('Please check choices provided then try again.')