a = int(input("Enter the number of element : "))
l = []
for i in range(a) : l.append(int(input("Enter the element : ")))
print("Even numbers are : ", [i for i in l if i%2==0])
print("Odd numbers are : ", [i for i in l if i%2==1])