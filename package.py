class Package:
    def __init__(self, ID, address, city, zipcode, deadline, weight, status):
        self.ID = ID
        self.address = address
        self.city = city
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.status = status

    def __str__(self):
        return (f"ID: {self.ID}   "
                f"Address: {self.address}   "
                f"City: {self.city}   "
                f"Zipcode: {self.zipcode}   "
                f"Deadline: {self.deadline}   "
                f"Weight: {self.weight}   "
                f"Status: {self.status}")