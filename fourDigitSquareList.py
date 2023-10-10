from math import sqrt as s
a = int(input("enter the start : "))
b = int(input("enter the end : "))
start = -1
for i in range(a, b+1):
    if s(i) == int(s(i)):
        start = s(i)
        break

print([i for i in range(a, b+1) if s(i) == int(s(i)) and len(str(i)) == 4 and not [j for j in list(str(i)) if j%2==1]] or "no elements found")