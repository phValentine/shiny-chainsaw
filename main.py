import csv

from hashTable import HashTable
from truck import Truck
from package import Package


            # Reads the data from Packages.csv and makes a list for each row
with open("data/Packages.csv") as package_csv:
    Package_csv = csv.reader(package_csv)
    Package_csv = list(Package_csv)


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

            # Loads the data from Package.csv in package_hashmap
load_package_data("data/Packages.csv", package_hashmap)

print(package_hashmap.lookup(1))