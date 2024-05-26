# Creates package class
class Package:
    def __init__(self, ID, address, city, state, zipcode, deadline, weight, status):
        self.ID = ID
        self.address = address
        self.city = city
        self.sate = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.departure_time = None
        self.delivery_time = None

# Formatting for display information
    def __str__(self):
        return (f"ID: {self.ID}   "
                f"Address: {self.address}   "
                f"City: {self.city}   "
                f"State: {self.sate}   "
                f"Zipcode: {self.zipcode}   "
                f"Deadline: {self.deadline}   "
                f"Weight: {self.weight}   "
                f"Delivery: {self.delivery_time}"
                f"Status: {self.status}")

    def update_status(self, convert_timedelta):
        if self.delivery_time < convert_timedelta:
            self.status = "Delivered"
        elif self.delivery_time > convert_timedelta:
            self.status = "En route"
        else:
            self.status = "At hub"
