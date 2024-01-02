import csv
with open("program41.csv", "r") as file:
    contents = csv.DictReader(file)
    print("ID STUDENT-NAME\n--------------")
    for content in contents:
        print(content["id"], content["first_name"]+content["last_name"])
