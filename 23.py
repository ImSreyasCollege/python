# from math import sqrt as s
# a = int(input("enter the start : "))
# b = int(input("enter the end : "))

# list = [i for i in range(a, b+1) if s(i) == int(s(i)) and len(str(i)) == 4]
# final = []
# for num in list:
#     count = 0
#     for d in str(num):
#         if int(d)%2!=0 : count = count + 1
#     if count == 0 : final.append(num)
# print("List : ", final or "no numbers found")

print([i for i in range(int(input("Start : ")), int(input("End : "))+1) if len(str(i))==4 and int(i**0.5)**2==i and all([int(j)%2==0 for j in str(i)])] or "List is empty")

