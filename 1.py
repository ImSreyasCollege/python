x = int(input("enter the starting year : "))
y = int(input("enter the ending year : "))
for i in range(x, y + 1):
    if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
        print(i)
