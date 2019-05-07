#
#  CSE_322_combo_menu_driver.py
#  Author: Joan Goldberg
#  Date: 5/5/2019
#
#  PLTW Activity 3.2.2 Combo Menu with Order Class
#
#This line of code tells the Python interpreter that it needs to reference the 
#CSE_322_combo_class.py file.
from CSE_322_combo_class import Order

def main():
    print("*** Welcome to My Restaurant ***")

    # Initialize variables
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
    
        order.set_order(order.type_sandwich, order.price_sandwich, order.size_beverage, order.price_beverage, order.size_frenchfries, order.price_frenchfries, order.num_ketchups, order.discount)
        order_list.append(order)
        
        flag_another_order=(raw_input(order.name + ", "+ "would you like to order more? Y/N: ")).upper()    
    
    
    #Print the Total Cost
    cost=0
    for each_order in order_list:
        cost=cost+each_order.get_cost()
    print("Total cost of your order is: $" + str(cost))  
    
    #Print the order. print calls the method __str__() for a user defined class. 
    for each_order in order_list:
        print each_order 
        #print each_order.__str__()
        
        
    print("Thank you for your order!")



def sandwich(order):    
    #Sandwich Menu
    flag_sandwich=(raw_input("Hi " + order.name + ", " + "Do you want a sandwich? Y/N: ")).upper()    
    if flag_sandwich=="Y":
        print("* Sandwich Menu *")
        print("chicken $5.25")
        print("beef $6.25")
        print("tofu $5.75")
        
        order.type_sandwich=(raw_input("What type of sandwich would you like? chicken, beef or tofu): ")).upper()
        if order.type_sandwich == "CHICKEN" or order.type_sandwich == "BEEF" or order.type_sandwich == "TOFU":
            if order.type_sandwich == "CHICKEN":
                order.price_sandwich= 5.25
            elif order.type_sandwich == "BEEF":
                order.price_sandwich= 6.25
            else:
                order.price_sandwich= 5.75
        else:
            order.type_sandwich=""
    
def beverage(order):    
    #Beverage Menu    
    flag_beverage=(raw_input("Do you want a beverage? Y/N: ")).upper()    
    if flag_beverage=="Y":
        print("* Beverage Menu *")
        print("small $1.00")
        print("medium $1.75")
        print("large $2.25")
        order.size_beverage=(raw_input("What size would you like? S/M/L: ")).upper()
        if order.size_beverage=="S" or order.size_beverage=="M" or order.size_beverage=="L":
            if order.size_beverage == "S":
                order.price_beverage=1.00
            elif order.size_beverage == "M":
                order.price_beverage=1.75
            else:
                order.price_beverage=2.25
        else:
            order.size_beverage = ""

def frenchfries(order):
    #French Fries Menu    
    flag_frenchfries=(raw_input("Do you want french fries? Y/N: ")).upper()    
    if flag_frenchfries=="Y":
        print("* French Fries Menu *")
        print("small $1.00")
        print("medium $1.50")
        print("large $2.00")
        order.size_frenchfries=(raw_input("What size would you like? S/M/L: ")).upper()
        if order.size_frenchfries=="S" or order.size_frenchfries=="M" or order.size_frenchfries=="L":
            if order.size_frenchfries == "S":
                flag_frenchfries=(raw_input("Do you want to mega size your french fries? Y/N: ")).upper()    
                if flag_frenchfries=="Y":
                    order.size_frenchfries="L"
                    order.price_frenchfries=2.00
                else:    
                    order.price_frenchfries=1.00
            elif order.size_frenchfries == "M":
                order.price_frenchfries=1.50
            else:
                order.price_frenchfries=2.00
        else:
            order.size_frenchfries=""
    
def ketchup(order):    
    #Ketchup    
    order.num_ketchups=input("How many ketchup packets would you like? Cost $0.25 each: ")
    
def take_discount(order):    
    #Discount
    if order.type_sandwich!="" and order.size_beverage!="" and order.size_frenchfries!="":
        order.discount=-1

#main program
main()
