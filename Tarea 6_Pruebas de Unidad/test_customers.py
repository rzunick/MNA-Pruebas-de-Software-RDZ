# test_customer.py
import unittest
from customer import Customer
from file_operations import read_data_from_file

class TestCustomerMethods(unittest.TestCase):
    def test_create_customer(self):
        # Arrange
        customer = Customer(name="Jane Doe", email="janedoe@example.com")
        
        # Act
        customer.save()
        data = read_data_from_file("customers.json")
        
        # Assert
        self.assertTrue(any(c['name'] == "Jane Doe" for c in data), "Customer should be created and found in the file.")

if __name__ == '__main__':
    unittest.main()

