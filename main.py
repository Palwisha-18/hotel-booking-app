import pandas as pd

df = pd.read_csv("hotels.csv", dtype={"id": str})
df_cards = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")
df_card_security = pd.read_csv("card_security.csv", dtype=str)


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df['id'] == self.hotel_id, "name"].squeeze()

    def is_available(self):
        availability = df.loc[df['id'] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
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


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, cvc):
        card_data = {
           "number": self.number,
           "expiration": expiration,
           "cvc": cvc,
           "holder": holder
        }
        if card_data in df_cards:
            return True

        return False


class SecureCreditCard(CreditCard):
    def authenticate(self, user_entered_password):
        password = df_card_security.loc[df_card_security['number'] == self.number, "password"].squeeze()
        if password == user_entered_password:
            return True
        return False


print(df)
print(df_cards)
print(df_card_security)
hotel_id = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_id)
if hotel.is_available():
    card_number = input("Enter Credit Card number: ")
    credit_card = SecureCreditCard(card_number)
    expiration_date = input("Enter Expiration Date: ")
    cvc = input("Enter CVC number: ")
    holder_name = input("Enter Holder name: ")
    user_password = input("Enter Credit Card password: ")
    if credit_card.validate(expiration_date, holder_name, cvc) and credit_card.authenticate(user_password):
        hotel.book()
        name = input("Enter your name: ")
        reservation_ticket = ReservationTicket(name, hotel)
        print(reservation_ticket.generate())
    else:
        print("Invalid Card Details")
else:
    print("Hotel is fully booked!")
