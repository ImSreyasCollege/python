from csv import reader
with open("csv3.csv", newline='') as csvfile:
    d = reader(csvfile, delimiter=' ', quotechar='|')
    for i in d:
        print(', '.join(i))
