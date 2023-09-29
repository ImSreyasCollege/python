n = int(input("enter the number of elements in the first list : "))
a = []
b = []
sum1 = 0
sum2 = 0
for i in range(0, n):
    a.append(int(input(f"enter the {i + 1} element : ")))
m = int(input("enter the number of elements in the second list : "))
for i in range(0, m):
    b.append(int(input(f"enter the {i + 1} element : ")))

print(f"\nlength of first list is : {len(a)}")
print(f"length of second list is : {len(b)}")
print("two list have same number of elements" if len(a) == len(b) else "two list have different number of elements")

for i in range(0, n):
    sum1 = sum1 + a[i]
for i in range(0, m):
    sum2 = sum2 + b[i]
print(f"\nsum of all elements in the first list is : {sum1}")
print(f"sum of all elements in the second list is : {sum2}")
print("sum is same" if sum1 == sum2 else "sum is not same")

val = [i for i in a if i in b]
print("\nany value occur in both : " + ("false" if len(val) == 0 else "true"))
print(val if len(val) != 0 else "")
