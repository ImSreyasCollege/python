import csv

with open("name.csv", "r") as file :
    # print(file.read())
    contents = csv.DictReader(file)
    for content in contents :
        print(content["name"])
