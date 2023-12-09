import csv
with open("program41.csv", newline='') as csvfile:
    d = csv.DictReader(csvfile)
    print(" ID    STUDENTNAME")
    print("--------------------")
    for i in d:
        print(i['id'],i['first_name'])
