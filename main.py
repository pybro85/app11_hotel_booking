import pandas

df = pandas.read_csv("hotels.csv", dtype={"id": str})


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[
            df["id"] == self.hotel_id, "name"
        ].squeeze()  # squuese method extracts the string

    def avaliable(self):
        """Checks if the hotel is available"""
        avaliability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if avaliability == "yes":
            return True
        else:
            return False

    def book(self):
        """Book a hotel by changing its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object 

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are your booking details:
        Name: {self.customer_name}
        Hotel name: {self.hotel.name}
        """
        return content

print(df)

hotel_ID = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_ID)
if hotel.avaliable():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
    print(reservation_ticket.generate())
else:
    print("Sorry, that hotel has no vacant rooms")
