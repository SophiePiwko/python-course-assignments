import sys
import math

if len(sys.argv) != 2:
   sys.exit("Needs one argument")

radius = float(sys.argv[1])
area = math.pi * radius ** 2
circumference = math.pi * 2 * radius
print("The area is ", area)
print("The circumference is ", circumference)

