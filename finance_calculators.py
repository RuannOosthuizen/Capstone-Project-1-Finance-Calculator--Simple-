import math

# The user is able to input if they would like their interest rate for their investment to be calculated or the bond they have to pay per month calculated.
# This program outputs the calculated the final amount of an investment with interest rates according to the information the user inputted.
# Similarly the program outputs the calculated bond repayment per month according to the information the user inputted.

print("investment - to calculate the amount of interest you'll earn on your investment.\nbond       - to calculate the amount you'll have to pay on a home loan\n")

# The user inputs what type of calculations they want.
answer = input("enter either 'investment' or 'bond' from the menu above to proceed: ")

# Investment calculations according to the information the user inputs:
if answer.lower() == "investment":
    # Information for the calculation.
    deposit = int(input("How much would you like to initially invest?\n :R"))
    invest_rate = int(input("Please enter the interest rate of your investment.\n :"))
    invest_rate_percentage = invest_rate / 100
    years = int(input("Please enter the number of years you would like to invest for.\n :"))
    interest = input("Would you like simple or compound interest?\nPlease type out your answer here (simple or compound): ")
    
    # simple interest rate type:
    if interest.lower() == "simple":
        simple_total = deposit * (1 + invest_rate_percentage * years)
        print(f"The total amount of your investment at the end of the investing period will be.\n :R{round(simple_total, 2)}")
    
    # compunded interest rate type:
    elif interest.lower() == "compound":
        comp_total = deposit * math.pow((1 + invest_rate_percentage) , years)
        print(f"The total amount of your investment at the end of the investing peroud will be.\n :R{round(comp_total, 2)}")

# Bond calculations according to the information the user inputs.
elif answer.lower() == "bond":
    # Information for the calculation.
    bond_amount = int(input("Please enter the present value of the house.\n :R"))
    bond_rate = int(input("Please enter the interest rate on the bond.\n :"))
    bond_rate_percentage = (bond_rate / 100) / 12
    months = int(input("Please enter the number of months you plan on to take to repay the bond.\n :"))

    # Calculated bond repayment per month
    bond_total = (bond_rate_percentage * bond_amount) / (1 - (1 + bond_rate_percentage) ** (-months))
    print(f"The total amount you would have to pay per month on the bond is.\n :R{round(bond_total, 2)} per month.")
 
 # If the user typed their answer incorrectly.
else:
    print("Please make sure you've entere 'Bond' or 'Investment' correctly.")
