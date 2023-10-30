a = input("enter a string : ")
print(a[0] + "".join(["$" if i == a[0] else i for i in a[1:]]))
