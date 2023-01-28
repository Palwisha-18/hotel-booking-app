import pandas as pd

df = pd.read_csv("hotels.txt")


class Hotel:

    def __init__(self, id):
        self.id = id

    def is_available(self):
        pass

    def book(self):
        pass


class ReservationTicket:
    def __init__(self, customer_name, hotel):
        pass

    def generate(self):
        pass


print(df)
id = input("Enter the id of the hotel: ")
hotel = Hotel(id)
if hotel.is_available():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(name, hotel)
    reservation_ticket.generate()
else:
    print("Hotel is fully booked!")
