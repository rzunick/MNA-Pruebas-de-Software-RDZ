# customer.py
from file_operations import read_data_from_file, write_data_to_file, generate_id

class Customer:
    def __init__(self, name, email):
        self.id = generate_id("customers.json")
        self.name = name
        self.email = email

    def save(self):
        data = read_data_from_file("customers.json")
        data.append(self.__dict__)
        write_data_to_file("customers.json", data)

    @staticmethod
    def delete(customer_id):
        data = read_data_from_file("customers.json")
        data = [customer for customer in data if customer['id'] != customer_id]
        write_data_to_file("customers.json", data)

    @staticmethod
    def display(customer_id):
        data = read_data_from_file("customers.json")
        customer = next((customer for customer in data if customer['id'] == customer_id), None)
        if customer:
            print(json.dumps(customer, indent=4))
        else:
            print("Customer not found.")

    @staticmethod
    def modify(customer_id, **kwargs):
        data = read_data_from_file("customers.json")
        for customer in data:
            if customer['id'] == customer_id:
                customer.update(kwargs)
                write_data_to_file("customers.json", data)
                return

