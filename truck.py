class Truck:
    def __init__(self, capacity, load, packages, speed, milage, address, departure_time):
        self.capacity = capacity
        self.load = load
        self.packages = packages
        self.speed = speed
        self.milage = milage
        self.address = address
        self.departure_time = departure_time

    def __str__(self):
        return (f"Capacity: {self.capacity}   "
                f"Load: {self.load}   "
                f"Packages: {self.packages}   "
                f"Speed: {self.speed}   "
                f"Milage: {self.milage}   "
                f"Address: {self.address}   "
                f"Departure time: {self.departure_time}   ")
