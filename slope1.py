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
#
# User enters the coordinates of 2 points (x1, y1) and (x2, y2)
# Verify the coordinates are numeric. 
inputError = False
x1=input("Enter x coordinate of point 1: ")
y1=input("Enter y coordinate of point 1: ")
x2=input("Enter x coordinate of point 2: ")
y2=input("Enter y coordinate of point 2: ")

if x1.isnumeric(): 
    x1=int(x1)
else:
    print ("Error: Enter a number for x1")
    inputError = True
    
if y1.isnumeric(): 
    y1=int(y1)
else:
    print ("Error: Enter a number for y1")
    inputError = True

if x2.isnumeric(): 
    x2=int(x2)
else:
    print ("Error: Enter a number for x2")
    inputError = True

if y2.isnumeric(): 
    y2=int(y2)
else:
    print ("Error: Enter a number for y2")    
    inputError = True

# Calculate the slope 

