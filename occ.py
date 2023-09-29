a = input("enter the total no.of name : ")
names = []
for i in range(0, int(a)):
    names.append(input(f"enter name {i+1} : "))
b = input("enter sub string to search : ")
print(f"total count is : {str(names).count(b)}")