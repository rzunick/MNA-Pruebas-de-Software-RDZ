# test_hotel.py
import unittest
from hotel import Hotel
from file_operations import read_data_from_file

class TestHotelMethods(unittest.TestCase):
    def test_create_hotel(self):
        # Arrange
        hotel = Hotel(name="Test Hotel", location="Test Location", rooms={"101": {"availability": True, "customer_id": None}})
        
        # Act
        hotel.save()
        data = read_data_from_file("hotels.json")
        
        # Assert
        self.assertTrue(any(h['name'] == "Test Hotel" for h in data), "Hotel should be created and found in the file.")

if __name__ == '__main__':
    unittest.main()

