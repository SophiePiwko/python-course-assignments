while True:
    height = float(input("height: "))
    if height < 0:
        print("The height can't be negative. Please enter a new height")
        
    width = float(input("width: "))
    if width < 0:
        print("The width can't be negative. Please enter a new width")
    
    break 

area = height * width 
perimeter = 2 * (height + width)

print("The area of the rectangle is " + str(area) + ".")
print("The perimeter of the rectangle is " +str(perimeter) + ".")

    
    
