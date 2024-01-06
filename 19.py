n = int(input("enter the number of inputs : "))
a = []
for i in range(0, n):
    a.append(int(input(f"enter number {i+1} : ")))
print("List : ", a)
print("Final list : ", [i for i in a if i%2!=0])