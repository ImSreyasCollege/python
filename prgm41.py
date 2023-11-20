import csv
with open("csv3.csv", newline='') as csvfile:
    d = csv.DictReader(csvfile)
    print(" ID STUDENT NAME")
    print("--------------------")
    for i in d:
        print(i['id'],i['first_name'])
