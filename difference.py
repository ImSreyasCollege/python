x = input("enter the colors in the first list : ")
y = input("enter the colors in the second list : ")
out = set(x.replace(" ", "").split(",")).difference(set(y.replace(" ", "").split(",")))
print(out)