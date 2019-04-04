##
#  slope.py
#
#  Author: Mrs. Goldberg
#  Date: 4/3/2019
#
#  This program uses two points (x1, y1) and (x2, y2) to     
#  1. Calculate the slope of the line 
#  2. Find the equation of the line in slope intercept form
#  3. Find the equation of the line in point slope form
#
def main(x1, y1, x2, y2) :
    run = x2-x1
    rise = y2-y1 
    if run == 0:
        verticalLine(x1)
    elif rise == 0:
        horizontalLine(y1)
    else:
        diagonalLine(x1, y1, rise/run)
         
    
## 
#  Vertical Line
#
def verticalLine(x1) :
    print ("slope is undefined")
    print ("x = ", x1)
    
## 
#  Horizontal Line
#
def horizontalLine(y1) :
    print ("slope = 0")
    print ("y = ", y1)    
    
## 
#  Diagonal Line
#
def diagonalLine(x1, y1, m) :
    print ("slope = ", m)
    yIntercept = y1 - (m * x1)
    print ("y = "+str(m)+"x"+" + "+str(yIntercept)) 
    print ("(y - "+str(y1)+") = "+str(m)+"(x - " + str(x1) + ")")
    
# Start the program.
# Testcase #1 Diagonal Line Positive Slope
print()
print("Testcase #1 Diagonal Line")
ix1 = -2
iy1 = 0 
ix2 = 0
iy2 = 4
main(ix1, iy1, ix2, iy2)

# Testcase #2 Vertical Line
print()
print("Testcase #2 Vertical Line")
ix1 = -2
iy1 = 0 
ix2 = -2
iy2 = 4
main(ix1, iy1, ix2, iy2)

# Testcase #3 Horizontal Line
print()
print("Testcase #3 Horizontal Line")
ix1 = -8
iy1 = 3 
ix2 = 2
iy2 = 3
main(ix1, iy1, ix2, iy2)
