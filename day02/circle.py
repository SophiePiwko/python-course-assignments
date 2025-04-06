import math

while True:
    radius = float(input("radius: "))
    if radius < 0:
        print("The radius can't be negative. Please enter a new radius")
    else:
        break

area = math.pi*radius**2
circumference = math.pi*2*radius
print("The area is " + str(area) + ".")
print("The circumference is " + str(circumference) + ".")

