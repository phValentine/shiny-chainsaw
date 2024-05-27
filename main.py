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
def extract_address(address):
    for row in Node_csv:
        if address in row[2]:
            return int(row[0])


# Test address
def test_extract_address():
    print(extract_address('177 W Price Ave') == 4)  # Pass
    print(extract_address('4001 South 700 East') == 0)  # Pass
    print(extract_address('6351 South 900 East') == 26)  # Pass
    print(extract_address('380 W 2880 S') == 18)  # Pass


#test_extract_address()


# Makes calling upon distance_between shorter and easier
def final_distance(node1, node2):
    distance = distance_between(extract_address(node1), extract_address(node2))
    return distance


truck1 = truck.Truck(16, None, [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40], 18, 0.0,
                     "4001 South 700 East", datetime.timedelta(hours=8))

truck2 = truck.Truck(16, None, [2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 17, 18, 21, 22, 36, 38], 18, 0.0,
                     "4001 South 700 East", datetime.timedelta(hours=10, minutes=20))

truck3 = truck.Truck(16, None, [6, 23, 24, 25, 26, 27, 28, 32, 33, 35, 39], 18, 0.0,
                     "4001 South 700 East", datetime.timedelta(hours=9, minutes=5))
# Core algorithm

# Interface
