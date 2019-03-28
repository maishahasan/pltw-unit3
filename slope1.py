# slope.py
#
# Author: Mrs. Goldberg
# Date: 3/27/2019
#
# Find the slope of a line given two points. 
#
# Inputs:
#   x1: x coordinate of point 1
#   y1: y coordinate of point 1
#   x2: x coordinate of point 2
#   y2: y coordinate of point 2
#
# Outputs:
#   m: slope of the line    

# Verify the coordinates are numeric. 
def validate_input(arg_x1,arg_y1,arg_x2,arg_y2):
    if not arg_x1.isnumeric(): 
        print ("Error: Enter a number for x1")
        return False
        
    if not arg_y1.isnumeric(): 
        print ("Error: Enter a number for y1")
        return False
    
    if not arg_x2.isnumeric(): 
        print ("Error: Enter a number for x2")
        return False
    
    if not arg_y2.isnumeric(): 
        print ("Error: Enter a number for y2")    
        return False

    return True

# main
# User enters the coordinates of 2 points (x1, y1) and (x2, y2)
x1=input("Enter x coordinate of point 1: ")
y1=input("Enter y coordinate of point 1: ")
x2=input("Enter x coordinate of point 2: ")
y2=input("Enter y coordinate of point 2: ")

# Calculate the slope 
if validate_input(x1,y1,x2,y2):
    x1=int(x1)
    y1=int(y1)
    x2=int(x2)
    y2=int(y2)
    
    
    
print("*** End of program ***")

