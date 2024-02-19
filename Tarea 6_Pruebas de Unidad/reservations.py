# reservations.py
from file_operations import read_data_from_file, write_data_to_file, generate_id
from datetime import datetime

class Reservation:
    def __init__(self, customer_id, hotel_id, start_date, end_date, room_number):
        self.id = generate_id("reservations.json")
        self.customer_id = customer_id
        self.hotel_id = hotel_id
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
        self.room_number = room_number

    def save(self):
        data = read_data_from_file("reservations.json")
        reservation_dict = self.__dict__
        reservation_dict['start_date'] = self.start_date.strftime("%Y-%m-%d")
        reservation_dict['end_date'] = self.end_date.strftime("%Y-%m-%d")
        data.append(reservation_dict)
        write_data_to_file("reservations.json", data)

    @staticmethod
    def cancel(reservation_id):
        data = read_data_from_file("reservations.json")
        data = [reservation for reservation in data if reservation['id'] != reservation_id]
        write_data_to_file("reservations.json", data)

    @staticmethod
    def display(reservation_id):
        data = read_data_from_file("reservations.json")
        reservation = next((reservation for reservation in data if reservation['id'] == reservation_id), None)
        if reservation:
            print(json.dumps(reservation, indent=4))
        else:
            print("Reservation not found.")

