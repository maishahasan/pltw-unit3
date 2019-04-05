##
#  ws-cmpnd-ifs.py
#  Author: Mrs. Goldberg
#  Date: 4/5/2019
#
def main():
    
    #example()
    ex1()
    ex2()
    ex3()
    
##
#  If the day is Friday, write, “Thank goodness it’s Friday.” 
#  Otherwise, write, “How long till Friday?”
def example():
    day = input("Enter a day of the week: ")
    if day == "Friday":
        print ("Thank goodness it's Friday")
    else:
        print ("How long till Friday?")

##
#  If the day is any day but “Monday” the program writes, “At least it’s not Monday.”
def ex1():
    day = input("Enter a day of the week: ")    


##
#  If the user is a teenager, the program writes, “You are a teenager.” 
#  Otherwise, it writes, “You are not a teenager.” 
#  (Remember that you can assume there is a variable called age that you can refer to.)
def ex2():
    age = int(input("Enter an age: "))
    
##    
# If the day is a weekend day, the program writes, “It is the weekend.” 
# Otherwise, it writes, “It is not the weekend.”
def ex3():  
    day = input("Enter a day of the week: ") 
    
    
# Start the program.
main()

