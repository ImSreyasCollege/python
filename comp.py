x = []

for i in range(0, int(input("enter the no.of elements : "))):
    x.append(int(input(f"enter a number {i + 1} : ")))

# absolute value of the numbers are
print("absolute values of the numbers are : ")
print([abs(i) for i in x])

# squares of the value
print("squares of the values are : ")
print([i*i for i in x])

# string contains any vowels
string = input("enter a string : ")
vowels = "aeiouAEIOU"
print([i for i in string if i in vowels])

# string to ord format
s = input("enter another string : ")
print([ord(i) for i in s])