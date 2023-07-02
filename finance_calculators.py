import math

# User will be asked to pick bond or investment

user_choice  = '''
"Choose either 'bond or investment to proceed.
investment - to calculate the amount of interest you'll earn on your investment
bond - to calculate the amount you'll have to pay on a home loan
Enter either 'investment' or 'bond' from the menu above to proceed:"

'''
print(user_choice)


user_input = input("> ").lower()

if user_input =="investment":
     
     amount = float(input("Please enter amount being invested :\n"))
     rate = float(input("Please enter the interest rate :\n"))
     years = float(input("Please enter the number of years you are planning on investing for :\n"))

     interest = input("'simple' or 'compound'").lower() #Users write Simple or Compound

     if interest == "simple":
    # Calculate simple interst
        total = amount * (1 +( rate /100) * years)
        print("The final amount with simple interest is " + str(total))
   
     elif interest == "compound": # If the User picks compound

        total = amount * math.pow((1 + (rate / 100)), years)
        print("The final amount with compound interest will be " + str(total))

     else:
        print("The option you chose is not valid, please choose from the options 'simple or 'compound' ")


elif user_input == "bond":
    house_value = float(input(" Please enter the value of house "))  
    yearly_interest_rate = float(input("User enters interest rate number")) 
    repay= int(input("User enters number of months which the bond will be repaid"))
# Below is the calcuation for bond repyaments
    monthly_interest_rate = (yearly_interest_rate / 12) / 100
    repayment =(monthly_interest_rate * house_value) / (1 -(1 + monthly_interest_rate)** (-repay)) 
    print(str(repayment))

else: 
    print(" The option you have chosen is invalid. Please start again and chose one of the options available")