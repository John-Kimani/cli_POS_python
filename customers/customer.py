import json
class CustomerProfile:
    '''
    Class that helps to generate instances for creating a new customer account on this application
    '''
    # initialize list of customers as empty as the class variable
    # customers_list = []

    def __init__(self, customer_id, customer_name, location, contact):
        '''
        Method that defines properties of this class.

        Args: 
            customer's name
            Their location and contact
        '''
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.location = location
        self.contact = contact

    def __repr__(self):
        '''
        Method to display customer profile with their name
        '''
        return f'name:{self.customer_name}, location:{self.location}, contact:{self.contact}'
    

    @classmethod
    def save_customer(cls, customer_name, location, contact):
        '''
        Method to create and save new customer infomation
        '''
        customers_database = 'database/customers.json'
        with open(customers_database, 'r') as customers_file:
            customer_accounts = json.load(customers_file)
            try:
                if customer_accounts == []:
                    id = 1
                    customer_id = 'C000' + str(id)
                    customer = {
                            "customer_id": customer_id,
                            "customer_name":customer_name,
                            "location": location,
                            "contact":contact
                        }
                elif customer_accounts !=[]:
                    id = 1
                    for customer in customer_accounts:
                        id = id + 1
                        customer_id = 'C000' + str(id)
                        customer = {
                            "customer_id": customer_id,
                            "customer_name":customer_name,
                            "location": location,
                            "contact":contact
                        }
                customer_accounts.append(customer)
                print('Please wait!! Saving to database...')
                with open(customers_database, "w") as customer_file:
                    json.dump(customer_accounts, customer_file, indent=4)
                    print("Customer Account Created Successfully")
            except:
                print("Unable to create customer account")

    @classmethod
    def show_all_customers(cls):
        '''
        Method to show all customer accounts
        '''
        customers_database = 'database/customers.json'
        with open(customers_database, 'r') as customers_file:
            customer_accounts = json.load(customers_file)
            i = 0
            for customer in customer_accounts:
                id = customer["customer_id"]
                name = customer["customer_name"]
                location = customer["location"]
                contact = customer["contact"]
                print(f"Customer ID: {id}")
                print(f"Customer Name: {name}")
                print(f"Customer Location: {location}")
                print(f"Customer Contact: {contact}")
                print('\n\n')
                i = i + 1

    @classmethod
    def update_customer_account(self, customer_id, customer_name, location, contact):
        '''
        Method to update customer instance
        '''
        customers_database = 'database/customers.json'
        file = open(customers_database, 'r')
        customer_accounts = json.load(file)
        for customer in customer_accounts:
            try:
                if customer.get("customer_id") == customer_id:
                    customer.update({
                            "customer_id": customer_id,
                            "customer_name":customer_name,
                            "location": location,
                            "contact":contact
                    })
                    print("Saving changes ...")
                with open(customers_database, 'w') as customers_file:
                    json.dump(customer_accounts, customers_file, indent=4)
            except:
                print("Unable to update")

        

    @classmethod
    def delete_customer(cls, id):
        '''
        Method to remove customer instance
        '''
        customers_database = 'database/customers.json'
        file = open(customers_database, 'r')
        customer_accounts = json.load(file)
        for customer in customer_accounts:
            if customer.get("customer_id") == id:
                customer_accounts.remove(customer)
                id = customer["customer_id"]
                name = customer["customer_name"]
                location = customer["location"]
                contact = customer["contact"]
                print(f"Customer ID: {id}")
                print(f"Customer Name: {name}")
                print(f"Customer Location: {location}")
                print(f"Customer Contact: {contact}")
                print('\n\n')
                with open(customers_database, 'w') as customers_file:
                    json.dump(customer_accounts, customers_file, indent=4)

    @classmethod
    def search_customer_by_name(cls, customer_name):
        '''
        Method to find customer by name

        Args: 
            customer name
        Return:
            Customer found in list
        '''
        customers_database = 'database/customers.json'
        isPresent = False
        with open(customers_database, 'r') as customers_file:
            customer_accounts = json.load(customers_file)
            for customer in customer_accounts:
                try: 
                    if customer.get("customer_name") == customer_name:
                        isPresent = True
                        print(customer)
                except:
                    print("No customer with such name")
            return isPresent

    @classmethod
    def search_customer_by_id(cls, customer_id):
        '''
        Method to search cutomer by ID
        '''
        customer_database = 'database/customers.json'
        with open(customer_database, 'r') as customers_file:
            customers = json.load(customers_file)
            customer = ""
            for customer in customers:
                if customer.get("customer_id") == customer_id:
                    customer = customer
                    break
            return customer

    @classmethod
    def customer_exist(cls, customer_name):
        '''
        Method to check customer account by name
        '''
        customers_database = 'database/customers.json'
        isPresent = False
        with open(customers_database, 'r') as customers_file:
            customer_accounts = json.load(customers_file)
            for customer in customer_accounts:
                try:
                    if customer.get("customer_name") == customer_name:
                        isPresent = True
                except:
                    print("No customer with such name")
            return isPresent

    @classmethod
    def customer_exist_by_id(cls, customer_id):
        '''
        Customer validation method 
        '''
        customers_database = 'database/customers.json'
        isPresent = False
        with open(customers_database, 'r') as customers_file:
            customer_accounts = json.load(customers_file)
            for customer in customer_accounts:
                if customer.get("customer_id") == customer_id:
                    isPresent = True
            return isPresent
                
