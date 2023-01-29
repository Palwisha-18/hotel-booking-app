import pandas as pd

df = pd.read_csv("hotels.csv", dtype={"id": str})


class Hotel:

    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df['id'] == self.hotel_id, "name"].squeeze()

    def is_available(self):
        availability = df.loc[df['id'] == self.hotel_id, "available"].squeeze()
        if availability:
            return True
        else:
            return False

    def book(self):
        df.loc[df['id'] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)


class ReservationTicket:
    def __init__(self, customer_name, hotel):
        self.customer_name = customer_name
        self.hotel = hotel

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are your reservation details:
        Name: {self.customer_name}
        Hotel: {self.hotel.name}
        """

        return content


print(df)
hotel_id = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_id)
if hotel.is_available():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(name, hotel)
    print(reservation_ticket.generate())
else:
    print("Hotel is fully booked!")
