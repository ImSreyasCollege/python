fruits = {"apple":2, "orange": 14, "pineapple": 31, "watermelon": 61, "grapes": 10}
asc = list(fruits.items())
asc.sort()
desc = list(fruits.items())
desc.sort(reverse=True)
print("Dictionary is : ", fruits, "\n")
print("Ascending order : ", asc)
print("Descending order : ", desc)
