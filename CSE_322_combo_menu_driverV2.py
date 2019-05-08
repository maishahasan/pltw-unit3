##  CSE_322_combo_menu_driverV2.py
#   Author: Joan Goldberg
#   Date: 5/5/2019
#
#   PLTW Activity 3.2.2 Combo Menu with Order Class
#

##  This line of code tells the Python interpreter that it needs to reference the 
#   CSE_322_combo_class.py file for the Order class.
#
from CSE_322_combo_classV2 import Order

def main():
    print("*** Welcome to My Restaurant ***")

##  The order is written to a list. 
#   The list is printed at the end of the program.
#
    order_list = []
    
    flag_another_order=(raw_input("Can I take your order? Y/N: ")).upper()    
    while flag_another_order == "Y": 
        name=(raw_input("What is your name? ")).upper()    
        order = Order(name)
    
        sandwich(order)
        beverage(order)
        frenchfries(order)
        ketchup(order)
        take_discount(order)
    
        #order.set_order(order.type_sandwich, order.price_sandwich, order.size_beverage, order.price_beverage, order.size_frenchfries, order.price_frenchfries, order.num_ketchups, order.discount)
        order_list.append(order)
        
        flag_another_order=(raw_input(order.name + ", "+ "would you like to order more? Y/N: ")).upper()    
    
##  Print the total cost of the order.
#    
    cost=0
    for each_order in order_list:
        cost=cost+each_order.calc_cost()
    print("Total cost of your order is: $" + str(cost))  
    
##  Print the order from the order list.
#   print is using the __str__() method.
#
    for each_order in order_list:
        print each_order

    print("Thank you for your order!")


##  Sandwich Menu
#
def sandwich(order):    
    flag_sandwich=(raw_input("Hi " + order.name + ", " + "Do you want a sandwich? Y/N: ")).upper()    
    if flag_sandwich=="Y":
        print("* Sandwich Menu *")
        print("chicken $5.25")
        print("beef $6.25")
        print("tofu $5.75")
        order.type_sandwich=(raw_input("What type of sandwich would you like? chicken, beef or tofu): ")).upper()
        if order.is_type_sandwich_valid():
            order.set_price_sandwich()
        else:    
            print (order.type_sandwich + " sandwich is not available.")
            order.type_sandwich = ""
            
##  Beverage Menu
#
def beverage(order):    
    flag_beverage=(raw_input("Do you want a beverage? Y/N: ")).upper()    
    if flag_beverage=="Y":
        print("* Beverage Menu *")
        print("small $1.00")
        print("medium $1.75")
        print("large $2.25")
        order.size_beverage=(raw_input("What size would you like? S/M/L: ")).upper()
        if order.is_size_beverage_valid():
            order.set_price_beverage()
        else:    
            print (order.size_beverage + " beverage is not available.")
            order.size_beverage = ""
                        
##  French Fries Menu
#
def frenchfries(order):
    flag_frenchfries=(raw_input("Do you want french fries? Y/N: ")).upper()    
    if flag_frenchfries=="Y":
        print("* French Fries Menu *")
        print("small $1.00")
        print("medium $1.50")
        print("large $2.00")
        order.size_frenchfries=(raw_input("What size would you like? S/M/L: ")).upper()
        if not order.is_size_frenchfries_valid():
            print (order.size_frenchfries + " french fries is not available.")
            order.size_frenchfries = ""
        elif order.size_frenchfries == "S":
            flag_frenchfries=(raw_input("Do you want to mega size your french fries? Y/N: ")).upper()    
            if flag_frenchfries=="Y":
                order.size_frenchfries="L"
            order.set_price_frenchfries()
            
##  Ketchup
#
def ketchup(order):    
    order.num_ketchups=input("How many ketchup packets would you like? Cost $0.25 each: ")
    
##  Discount
#
def take_discount(order):    
    if order.type_sandwich!="" and order.size_beverage!="" and order.size_frenchfries!="":
        order.discount=-1

##  main program
#
main()
