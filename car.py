##
#  car.py
#  Author: Mrs. Goldberg
#  Date: 4/9/2019
#
#  The Midtown Auto Company produced some models of cars that may be difficult to drive because the car wheels are not exactly round. 
#  Car models that exist are from 001 - 999. Cars with model numbers 100-200, 357, 468, 900-999 have been found to have this defect. 
#  Create a Defective Car Models application that allows customers to enter the model number of their car to find out if it is defective. 
#  If the user enters the model number of a car that is defective, display the message “Your car is defective. Please have it fixed”. 
#  If the user enters the model number of a car that is not defective, display the message “Your car is not defective”. 
#  If the user enters a model number that is not valid, display the message "Car model does not exist".
def main():
    model = input("Enter a car model: ") 
    length_model = len(model)
    if length_model == 3:
        if model >= "001" and model <= "999":
            if ((model >= "100" and model <= "200") or 
            model == "357" or
            model == "468" or 
            (model >= "900" and model <= "999")):
                print ("Car is defective")
            else:
                print ("Car is not defective")
        else:
            print ("Car model does not exist")
    else:
        print ("Car models are 3 numerals")
# Start the program.
main()
