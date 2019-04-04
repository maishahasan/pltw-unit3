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
def main() :
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
#  a is the x-intercept
#
def verticalLine(a) :
    print ("slope is undefined")
    print ("x = ", a)
    
## 
#  Horizontal Line
#  b is the y-intercept
#
def horizontalLine(b) :
    print ("slope = 0")
    print ("y = ", b)    
    
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
x1 = -2
y1 = 0 
x2 = 0
y2 = 4
main()

# Testcase #2 Vertical Line
print()
print("Testcase #2 Vertical Line")
x1 = -2
y1 = 0 
x2 = -2
y2 = 4
main()

# Testcase #3 Horizontal Line
print()
print("Testcase #3 Horizontal Line")
x1 = -8
y1 = 3 
x2 = 2
y2 = 3
main()
