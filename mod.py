from graphics.circle import area as areaOfCircle, perimeter as perimeterOfCircle
from graphics.rectangle import area as areaOfRectangle, perimeter as perimeterOfRectangle
from graphics._3Dgraphics.cuboid import area as areaOfCuboid, perimeter as perimeterOfCuboid
from graphics._3Dgraphics.sphere import area as areaOfSphere, perimeter as perimeterOfSphere

# circle 
r  = int(input("enter the radius of circle : "))
print("area of circle is : ", areaOfCircle(r))
print("perimeter of circle is : ", perimeterOfCircle(r), "\n")

# rectangle 
l = int(input("enter the length : "))
b = int(input("enter the breadth : "))
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





