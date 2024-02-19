# hotel.py
from file_operations import read_data_from_file, write_data_to_file, generate_id

class Hotel:
    def __init__(self, name, location, rooms):
        self.id = generate_id("hotels.json")
        self.name = name
        self.location = location
        self.rooms = rooms  # A dictionary of room_number: { "availability": True/False, "customer_id": None or customer ID }

    def save(self):
        data = read_data_from_file("hotels.json")
        data.append(self.__dict__)
        write_data_to_file("hotels.json", data)

    @staticmethod
    def delete(hotel_id):
        data = read_data_from_file("hotels.json")
        data = [hotel for hotel in data if hotel['id'] != hotel_id]
        write_data_to_file("hotels.json", data)

    @staticmethod
    def display(hotel_id):
        data = read_data_from_file("hotels.json")
        hotel = next((hotel for hotel in data if hotel['id'] == hotel_id), None)
        if hotel:
            print(json.dumps(hotel, indent=4))
        else:
            print("Hotel not found.")

    @staticmethod
    def modify(hotel_id, **kwargs):
        data = read_data_from_file("hotels.json")
        for hotel in data:
            if hotel['id'] == hotel_id:
                hotel.update(kwargs)
                write_data_to_file("hotels.json", data)
                return
        print("Hotel not found.")

    @staticmethod
    def reserve_room(hotel_id, room_number, customer_id):
        data = read_data_from_file("hotels.json")
        for hotel in data:
            if hotel['id'] == hotel_id:
                if room_number in hotel['rooms'] and hotel['rooms'][room_number]['availability']:
                    hotel['rooms'][room_number] = {"availability": False, "customer_id": customer_id}
                    write_data_to_file("hotels.json", data)
                    return True
        return False

    @staticmethod
    def cancel_reservation(hotel_id, room_number):
        data = read_data_from_file("hotels.json")
        for hotel in data:
            if hotel['id'] == hotel_id and not hotel['rooms'][room_number]['availability']:
                hotel['rooms'][room_number] = {"availability": True, "customer_id": None}
                write_data_to_file("hotels.json", data)
                return True
        return False
