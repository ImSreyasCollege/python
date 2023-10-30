n = int(input("enter the no.of elements : "))
words = []
max = 0
for i in range(n) : words.append(input("enter the word : "))
for word in words :
    if max<len(word) : max = len(word)
print(max)