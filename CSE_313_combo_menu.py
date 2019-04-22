#
#  CSE_313_combo_menu.py
#  Author: 
#  Date: 4/22/2019
#
#  PLTW Activity 3.1.3 Combo Menu
#  Python version 2.7   

print("*** Welcome to My Restaurant ***")
# Initialize variables
cost = 0

#Sandwich Menu
answer=(raw_input("Do you want a sandwich? Y/N: ")).upper()    
if answer == "Y":
    flag_sandwich = True
else:
    flag_sandwich = False
if flag_sandwich:
    print("* Sandwich Menu *")
    print("chicken $5.25")
    print("beef $6.25")
    print("tofu $5.75")
    
    type_sandwich=(raw_input("What type of sandwich would you like? chicken, beef or tofu): ")).upper()
    if type_sandwich == "CHICKEN" or type_sandwich == "BEEF" or type_sandwich == "TOFU":
        print("You ordered a " + type_sandwich + " sandwich")
        if type_sandwich == "CHICKEN":
            cost += 5.25
        elif type_sandwich == "BEEF":
            cost += 6.25
        else:
            cost += 5.75
    else:
        print("Error for sandwich")


#Beverage Menu    
answer=(raw_input("Do you want a beverage? Y/N: ")).upper()    
if answer == "Y":
    flag_beverage = True
else:
    flag_beverage = False
if flag_beverage:
    print("* Beverage Menu *")
    print("small $1.00")
    print("medium $1.75")
    print("large $2.25")
    size_beverage=(raw_input("What size would you like? S/M/L: ")).upper()
    if size_beverage=="S" or size_beverage=="M" or size_beverage=="L":
        print("You ordered a beverage " + size_beverage + " beverage")
        if size_beverage == "S":
            cost+=1.00
        elif size_beverage == "M":
            cost+=1.75
        else:
            cost+=2.25
    else:
        print("Error for beverage size")


#French Fries Menu    
answer=(raw_input("Do you want french fries? Y/N: ")).upper()    
if answer == "Y":
    flag_frenchfries = True
else:
    flag_frenchfries = False
if flag_frenchfries:
    print("* French Fries Menu *")
    print("small $1.00")
    print("medium $1.50")
    print("large $2.00")
    size_frenchfries=(raw_input("What size would you like? S/M/L: ")).upper()
    if size_frenchfries=="S" or size_frenchfries=="M" or size_frenchfries=="L":
        if size_frenchfries == "S":
            flag_frenchfries=(raw_input("Do you want to mega size your french fries? Y/N: ")).upper()    
            if flag_frenchfries=="Y":
                size_frenchfries="L"
                cost+=2.00
            else:    
                cost+=1.00
        elif size_frenchfries == "M":
            cost+=1.50
        else:
            cost+=2.00

        print("You ordered " + size_frenchfries + " french fries")
    else:
        print("Error for french fries size")


#Ketchup    
num_ketchup=input("How many ketchup packets would you like? Cost $0.25 each: ")
print("You ordered " + str(num_ketchup) + " packets of ketchup")
cost = cost + (num_ketchup * .25)

#Discount
if flag_sandwich and flag_beverage and flag_frenchfries:
    cost-=1
    
#Total Cost    
print("Total cost of your order is: " + str(cost))    
