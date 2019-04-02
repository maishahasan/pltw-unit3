# slope.py
#
# Author: Mrs. Goldberg
# Date: 3/27/2019
#
# Find the slope of a line given two points. 
# Write the equation of the line in 3 forms
# 1. slope intercept form
# 2. point slope form
# 3. standard form
#
# Inputs:
#   ix1: x coordinate of point 1
#   iy1: y coordinate of point 1
#   ix2: x coordinate of point 2
#   iy2: y coordinate of point 2
#
# Outputs:
#   m: slope of the line    

# Verify the coordinates are numeric. 
def isvalid(x1,y1,x2,y2):
    try:
        x1 = float(x1)
        y1 = float(y1)
        x2 = float(x2)
        y2 = float(y2)
    except ValueError:
        return False
    
    return True

# User enters the coordinates of 2 points (x1, y1) and (x2, y2)
ix1=input("Enter x coordinate of point 1: ")
iy1=input("Enter y coordinate of point 1: ")
ix2=input("Enter x coordinate of point 2: ")
iy2=input("Enter y coordinate of point 2: ")

# Calculate the slope 
if isvalid(ix1,iy1,ix2,iy2):
    ix1=float(ix1)
    iy1=float(iy1)
    ix2=float(ix2)
    iy2=float(iy2)
    
    
    
print("*** End of program ***")

