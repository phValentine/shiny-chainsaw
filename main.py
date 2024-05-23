import csv
import datetime

import truck
from hashTable import HashTable
from truck import Truck
from package import Package

# Reads the data from Packages.csv
with open("data/Packages.csv") as csvpackage:
    Package_csv = csv.reader(csvpackage)
    Package_csv = list(Package_csv)

    # Reads the data from Distances.csv
with open("data/Distance.csv") as csvdistance:
    Distance_csv = csv.reader(csvdistance)
    Distance_csv = list(Distance_csv)

    # Reads the data from Nodes.csv
with open("data/Nodes.csv") as csvnode:
    Node_csv = csv.reader(csvnode)
    Node_csv = list(Node_csv)


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
            pweight = package[6]
            pStatus = "processing"

            p = Package(pID, pAddress, pCity, pState, pZipcode, pDeadline, pweight, pStatus)

            package_hashmap.insert(pID, p)


# Creates the hash table that will store all the package data.
package_hashmap = HashTable()

# Loads the data from Package.csv in package_hashmap.
load_package_data("data/Packages.csv", package_hashmap)


# Finds the distance between two addresses, runs a reverse distance check if needed.
def distance_between(x, y):
    distance = Distance_csv[x][y]
    if distance == '':
        distance = Distance_csv[y][x]
    return float(distance)


truck1 = truck.Truck(16, None, [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40], 18, 0.0,
                     "4001 South 700 East", datetime.timedelta(hours=8))

truck2 = truck.Truck(16, None, [2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 17, 18, 21, 22, 36, 38], 18, 0.0,
                     "4001 South 700 East", datetime.timedelta(hours=10, minutes=20))

truck3 = truck.Truck(16, None, [6, 23, 24, 25, 26, 27, 28, 32, 33, 35, 39], 18, 0.0,
                     "4001 South 700 East", datetime.timedelta(hours=9, minutes=5))
