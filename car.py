##
#  car.py
#  Author: <your name>
#  Date: <today's date>
#
#  The Midtown Auto Company produced some models of cars that may be difficult to drive because the car wheels are not exactly round. 
#  Car models that exist are from 001 - 999. Cars with model numbers 100-200, 357, 468, 900-999 have been found to have this defect. 
#  Create a Defective Car Models application that allows customers to enter the model number of their car to find out if it is defective. 
#  If the user enters the model number of a car that is defective, display the message “Your car is defective. Please have it fixed”. 
#  If the user enters the model number of a car that is not defective, display the message “Your car is not defective”. 
#  If the user enters a model number that is not valid, display the message "Car model does not exist".
def main():
  model = input("Enter a car model: ") 
  # should model be cast to an int? float? or leave as a string? 
  # if model is a string, you need to check the length. 
  # len_model = len(model)
  
    
# Start the program.
main()
