a = int(input("enter the first number : "))
b = int(input("enter the second number : "))
c = int(input("enter the third number : "))

lar = a if a > b else b
print("largest number is : ", lar if lar > c else c)

