class rectangle: 
    def __init__(self, l, b):
        self.l = l
        self.b = b
    def area(self):
        return self.l*self.b
    def perimeter(self):
        return 2*(self.l+self.b)
    def comp(self, obj):
        if self.area() == obj.area():
            return "area of rectangles are equal"
        elif self.area() < obj.area():
            return "area of rectangle is lesser"
        else : 
            return "area of rectangle is greater"

l1 = int(input("enter the length of first rectangle : "))
b1 = int(input("enter the breadth of first rectangle : "))

l2 = int(input("enter the length of second rectangle : "))
b2 = int(input("enter the breadth of second rectangle : "))

obj1 = rectangle(l1, b1)
obj2 = rectangle(l2, b2)
print("\narea of first rectangle is : ", obj1.area())
print("perimeter of first rectangle is : ", obj1.perimeter())
print("\narea of second rectangle is : ", obj2.area())
print("perimeter of second rectangle is : ", obj2.perimeter())
print(obj1.comp(obj2))