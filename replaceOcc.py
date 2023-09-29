a = input("enter a string : ")
# b = [a[0]]
# for i in range(1, len(a)):
#     b.append("$" if a[i] == a[0] else a[i])
# print("".join(b))
print(a[0] + "".join(["$" if i == a[0] else i for i in a[1:]]))
