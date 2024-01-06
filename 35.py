class Rectangle:
    def __init__(self, l, b):
        self.l = l
        self.b = b
    def area(self):
        return self.l * self.b
    def __lt__(self, obj):
        if self.area() == obj.area() :
            return "area of two rectangle is equal."
        if self.area() < obj.area() :
            return "area of rectangle 1 is lesser than rectangle 2."
        else :
            return "area of rectangle 2 is lesser than rectangle 1."

l1 = int(input("enter the length of the first rectangle : "))
b1 = int(input("enter the breadth of the first rectangle : "))
l2 = int(input("enter the length of the second rectangle : "))
b2 = int(input("enter the breadth of the second rectangle : "))
obj1 = Rectangle(l1, b1)
print("area of rectangle 1 is : ", obj1.area())
obj2 = Rectangle(l2, b2)
print("area of rectangle 2 is : ", obj2.area())

print(obj1 < obj2)
