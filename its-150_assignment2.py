#Eric Peterson
#31Jul2020
#ITS-150
#Comp Prog

# Fuel Efficiency Calculator for Journey with Multiple Legs


def main ():
    
    odom1 = eval(input("Please enter the starting odometer reading: "))
#Initial user input request
    
    print("Please enter your odometer reading and gallons of gasused on each leg of the trip.")
    print("When you have entered data for all the legs, then enter -1 for any of them.")
# User instructions

    miles_list = []
    gas_list = []
#Declaring lists for storing of data
    
    odom2 = ("Enter the odometer reading: ")
    
    gas = ("Enter gallons used: ")

    
    while odom2 != -1:
# While loop to be termintated when user input is equal to -1.

        odom2 = eval(input("Enter the odometer reading: "))
        gas = eval(input("Enter gallons used: "))
# User input request, eval is used to evaluate the input
       
        miles_list.append(odom2 - odom1)
        gas_list.append(gas)
# List instructions, for the miles_list, before storing it subtracts the previous mileage from the current
# to give us the distance traveled since the last leg.

        odom1 = odom2
# Instructs program to change the name of var odom2 to odom1 on the next iteration.

        for i in range(len(miles_list)):
            
            mpg = miles_list[i] / gas_list[i]
            
            print("The MPG for leg", i + 1, "of the journey is: {0:5.2f}".format(mpg))
# Prints the mpg for the given leg, i + 1 keeps track of what leg it currently is. mpg is the equation that is run.
                  
        total_miles = sum(miles_list)
        
        total_gas = sum(gas_list)
        
        print("Total MPG: {0:5.2f}".format(total_miles / total_gas))
# Final statement to print and run, gives total trip distance by adding up all of the miles_list entries.
# Also displays how much gas has been used by adding up all entries in the gas list.
# Have still been working on the exit command, it stores the -1 command, I know I have something wrong or missing,
# jsut cant quite put my finger on it.

main()
