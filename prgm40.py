from csv import reader
with open("program40.csv") as csvfile:
    readerFile = reader(csvfile)
    readerList = []
    for row in readerFile :
        readerList.extend(",".join(row).strip().split(","))
        # print(', '.join(row))
    print(readerList)
