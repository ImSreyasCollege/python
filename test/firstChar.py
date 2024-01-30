string = input("Enter a string : ")
count = {}
for char in string : count[char] = count[char]+1 if char in count else 1
print(count)