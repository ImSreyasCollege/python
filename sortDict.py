dict = {'apple': 2, 'orange': 3, 'mango': 8, 'strawberry': 5, 'pineapple': 4, 'watermelon': 7}
l = list(dict.items())
l.sort()
print(l)
l.sort(reverse=True)
print(l)