import csv


                    # Package reader


package_csv = 'data/Packages.csv'

with open(package_csv, 'r') as csvfile:
    package_reader = csv.DictReader(csvfile)




                    # Address reader


address_csv = 'data/Nodes.csv'

with open(address_csv, 'r') as csvfile:
    address_reader = csv.DictReader(csvfile)





                    # Distance reader


distance_csv = 'data/Distance.csv'

with open(distance_csv, 'r') as csvfile:
    distance_reader = csv.DictReader(csvfile)
