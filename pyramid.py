n = int(input("enter the step count : "))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(f"{j*i}\t", end="")
    print("\n")