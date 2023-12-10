# a = open("demo.txt", "r")
# b = open("t", "w")
# c = a.readlines()
# l = len(c)
# for i in range(0, l):
#   if i%2 == 0 :
#       b.write(c[i])
# b.close()
# b = open("t", "r")
# e = b.read()
# print(e)
# a.close()
# b.close()
with open("demo.txt", "r") as readFile:
    lines = readFile.readlines()
    with open("new.txt", "w") as writeFile:
        for i in range(0, len(lines), 2):
            writeFile.write(lines[i])
with open("new.txt", "r") as displayFile :
    print(displayFile.read())