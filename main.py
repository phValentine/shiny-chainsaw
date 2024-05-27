# C1. :IDENTIFICATION INFORMATION
# Name - Nicholas Noto      Student ID - 009077293
import csv
import datetime

import truck
from hashTable import HashTable
from package import Package

# Reads the data from Packages.csv
with open("data/Packages.csv") as csvpackage:
    Package_csv = csv.reader(csvpackage)
    Package_csv = list(Package_csv)
    # Read test
    # print(Package_csv)

# Reads the data from Distances.csv
with open("data/Distance.csv") as csvdistance:
    Distance_csv = csv.reader(csvdistance)
    Distance_csv = list(Distance_csv)
    # Read test
    # print(Distance_csv)

# Reads the data from Nodes.csv
with open("data/Nodes.csv") as csvnode:
    Node_csv = csv.reader(csvnode)
    Node_csv = list(Node_csv)
    # Read test
    # print(Node_csv)


# Reads package data and inserts it into the hashmap
def load_package_data(filename, package_hash):
    with open(filename) as package_info:
        package_data = csv.reader(package_info)
        for package in package_data:
            pID = int(package[0])
            pAddress = package[1]
            pCity = package[2]
            pState = package[3]
            pZipcode = package[4]
            pDeadline = package[5]
            pWeight = package[6]
            pStatus = "processing"

            p = Package(pID, pAddress, pCity, pState, pZipcode, pDeadline, pWeight, pStatus)

            package_hash.insert(pID, p)


# Creates the hash table that will store all the package data.
package_hashmap = HashTable()

# Loads the data from Package.csv in package_hashmap.
load_package_data("data/Packages.csv", package_hashmap)


# Find distance, information pulled from Distance.csv
# Only called upon by final_distance
def distance_between(node1, node2):
    distance = Distance_csv[node1][node2]
    if distance == '':
        distance = Distance_csv[node2][node1]
    return float(distance)


# Test distance
def test_distance_between():
    print(distance_between(0, 1) == 7.2)  # Pass
    print(distance_between(0, 26) == 3.6)  # Pass
    print(distance_between(1, 0) == 7.2)  # Pass
    print(distance_between(26, 25) == 8.3)  # Pass


#test_distance_between()


# Extract Address, extracts distance from Node.csv and returns integer value
# Only called upon by final_distance
def address_id(address):
    for row in Node_csv:
        if address in row[2]:
            return int(row[0])


# Test address
def test_address_id():
    print(address_id('177 W Price Ave') == 4)  # Pass
    print(address_id('4001 South 700 East') == 0)  # Pass
    print(address_id('6351 South 900 East') == 26)  # Pass
    print(address_id('380 W 2880 S') == 18)  # Pass


#test_address_id()


# Makes calling upon distance_between shorter and easier
def final_distance(node1, node2):
    distance = distance_between(address_id(node1), address_id(node2))
    return distance


truck1 = truck.Truck(16, None, [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40], 18, 0.0,
                     "4001 South 700 East", datetime.timedelta(hours=8))

truck2 = truck.Truck(16, None, [2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 17, 18, 21, 22, 36, 38], 18, 0.0,
                     "4001 South 700 East", datetime.timedelta(hours=10, minutes=20))

truck3 = truck.Truck(16, None, [6, 23, 24, 25, 26, 27, 28, 32, 33, 35, 39], 18, 0.0,
                     "4001 South 700 East", datetime.timedelta(hours=9, minutes=5))


# Core algorithm
def deliver_packages(truck):
    # Makes array of packages to be delivered
    not_delivered = []
    for packageID in truck.packages:
        package = package_hashmap.lookup(packageID)
        not_delivered.append(package)

    # clear truck package list for new order
    truck.packages.clear()

    # Cycles until all packages are delivered
    while len(not_delivered) > 0:
        next_address = 3000
        next_package = None
        # Nearest neighbor algorithm
        for package in not_delivered:
            if final_distance(truck.address, package.address) <= next_address:
                next_address = final_distance(truck.address, package.address)
                next_package = package

        # Construct new truck package list and remove the package from not_delivered
        truck.packages.append(next_package.ID)
        not_delivered.remove(next_package)

        # updates trucks mileage for each address
        truck.mileage += next_address
        truck.address = next_package.address

        # Update trucks time
        truck.time += datetime.timedelta(hours=next_address / 18)
        next_package.delivery_time = truck.time
        next_package.departure_time = truck.departure_time


deliver_packages(truck1)
deliver_packages(truck3)
# Accounts for only having 2 drivers, truck 2 cannot leave until one of the other trucks get back
truck2.departure_time = min(truck1.time, truck3.time)
deliver_packages(truck2)


# Interface
class Interface:
    # Welcome message
    print('Welcome to WGUPS')
    miles = truck1.mileage + truck2.mileage + truck3.mileage
    print("Today's mileage:", miles)
    limit = 140
    difference = limit - miles
    print("That's", f"{difference:.3}", "miles less than our limit of", limit, "miles!")
    print("The last package was delivered at : 12:29")

    print('')

    # Ask for input to continue
    text = input("For more information type: 'info'     ")
    if text == 'info':
        try:
            # Get the time that is wanted
            print("Enter a time in which you would like to pull the information from.")
            user_time = input("format: HH:MM (24 hour)        ")
            (h, m) = user_time.split(':')
            convert_timedelta = datetime.timedelta(hours=int(h), minutes=int(m))

            # Determines if all packages are needed to be printed or just one
            print("What would you like to know about this time?")
            package_selection = input("Enter 'one' for information on an individual package "
                                      "or 'all' for all packages.      ")
            # Prints just one package
            if package_selection == 'one':
                try:
                    packageID = input("Enter the package ID you are looking for:        ")
                    package = package_hashmap.lookup(int(packageID))
                    package.update_status(convert_timedelta)
                    print(str(package))
                # Ends program
                except ValueError:
                    print("No")
                    exit()

            # Prints all packages
            elif package_selection == 'all':
                try:
                    for packageID in range(1, 41):
                        package = package_hashmap.lookup(packageID)
                        package.update_status(convert_timedelta)
                        print(str(package))
                # Ends program
                except ValueError:
                    print("NO")
                    exit()
        # Ends program
        except ValueError:
            print("NO")
            exit()
