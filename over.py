n = int(input("enter the total no.of inputs : "))
a = []
for i in range(0, n):
    num = int(input(f"enter the number {i+1} : "));
    a.append(num if num <= 100 else "over")

print(a)