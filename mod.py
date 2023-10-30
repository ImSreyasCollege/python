from graphics.circle import *
from graphics.rectangle import area as areaOfRectangle, perimeter as perimeterOfRectangle
from graphics._3Dgraphics.cuboid import area as areaOfCuboid, perimeter as perimeterOfCuboid
from graphics._3Dgraphics.sphere import area as areaOfSphere, perimeter as perimeterOfSphere

# circle 
r  = int(input("enter the radius of circle : "))
print("area of circle is : ", area(r))
print("perimeter of circle is : ", perimeter(r), "\n")

# rectangle 
l = int(input("enter the length of rectangle : "))
b = int(input("enter the breadth of rectangle : "))
print("area of rectangle is : ", areaOfRectangle(l, b))
print("perimeter of rectangle is : ", perimeterOfRectangle(l, b), "\n")

# cuboid 
a = int(input("enter the side of cuboid : "))
print("area of the cuboid is : ", areaOfCuboid(a), "\n")
print("perimeter of cuboid is : ", perimeterOfCuboid(a), "\n")

# sphere
s = int(input("enter the radius of sphere : "))
print("area of the sphere is : ", areaOfSphere(s), "\n")
print("perimeter of sphere is : ", perimeterOfSphere(s), "\n")





