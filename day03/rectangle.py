import sys

if len(sys.argv) != 3:
    print("Usage: python script_name.py <height> <width>")
    sys.exit(1)

height = float(sys.argv[1])
width = float(sys.argv[2])

area = height * width
perimeter = 2 * (height + width)

print("The area of the rectangle is ", area)
print("The perimeter of the rectangle is ", perimeter)
    
    
