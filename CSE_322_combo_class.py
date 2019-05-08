## This module defines a class that models a restaurant order.
#

## The order has a sandwich, beverage, french fries and ketchup.
#  There is a $1 discount if a sandwich, beverage and french fries are ordered.
#
class Order:
    ## Constructs an order with a given name.
    #  The constructor is the first method in the class.
    #  The constructor initalizes the data attributes (properties).
    #  __init__ is the constructor. 
    #  self refers to the object
    #
    def __init__(self, name):
        self.name = name
        self.type_sandwich = ""
        self.price_sandwich = 0.00
        self.size_beverage = ""
        self.price_beverage = 0.00
        self.size_frenchfries = ""
        self.price_frenchfries = 0.00
        self.num_ketchups = 0
        self.discount = 0

    ## Sets the attributes of the order. 
    # 
    def set_order(self, type_sandwich, price_sandwich, size_beverage, price_beverage, size_frenchfries, price_frenchfries, num_ketchups, discount):
        self.type_sandwich = type_sandwich
        self.price_sandwich = price_sandwich
        self.size_beverage = size_beverage
        self.price_beverage = price_beverage
        self.size_frenchfries = size_frenchfries
        self.price_frenchfries = price_frenchfries
        self.num_ketchups = num_ketchups
        self.discount = discount

    ## Gets the price of the sandwich. 
    # 
    def get_price_sandwich(self):
            return self.price_sandwich

    ## Gets the price of the beverage. 
    # 
    def get_price_beverage(self):
            return self.price_beverage

    ## Gets the price of the french fries. 
    # 
    def get_price_frenchfries(self):
            return self.price_frenchfries

    ## Gets the number of ketchups ordered. 
    # 
    def get_num_ketchups(self):
            return self.num_ketchups

    ## Gets the discount for the order. 
    # 
    def get_discount(self):
            return self.discount

    ## Calculates the cost of the order. 
    # 
    def calc_cost(self):
        cost = self.price_sandwich + self.price_beverage + self.price_frenchfries + self.num_ketchups * .25 + self.discount
        return cost

    ## Returns the order in a string 
    # 
    def __str__(self):
        print_order = self.name + ", "
        if self.type_sandwich !="":
            print_order = print_order + self.type_sandwich + " sandwich, "
        if self.size_beverage != "":
            print_order = print_order + self.size_beverage + " beverage, "
        if self.size_frenchfries !="": 
            print_order = print_order + self.size_frenchfries + " french fries, "
        if self.num_ketchups > 0:
            print_order = print_order + str(self.num_ketchups) + " ketchup packets "
        if self.discount != 0:
            print_order = print_order + " $1 discount "
        
        return print_order
