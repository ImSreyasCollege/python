size = int(input("Enter the size : "))
for i in range(size+1) : 
    for j in range(i) : print("* ", end="")
    print("\n")
for i in range(size-1, 0, -1) :
    for j in range(i) : print("* ", end="")
    print("\n")