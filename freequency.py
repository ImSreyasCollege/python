str = input("enter a string : ")
collection = {}
for c in str : collection[c] = collection[c] + 1 if c in collection else 1
print(collection)