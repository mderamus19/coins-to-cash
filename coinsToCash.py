# Create a function called calc_dollars. In the function body, define a dictionary
# and store it in a variable named piggyBank. The dictionary should have the following
# keys defined.

# quarters
# nickels
# dimes
# pennies
# For each coin type, give yourself as many as you like.

# piggyBank = {
#     "pennies": 342,
#     "nickels": 9,
#     "dimes": 32
# }
# Once you have given yourself a large stash of coins in your piggybank,
# look at each key and perform the appropriate math on the integer value to
# determine how much money you have in dollars. Store that value in a variable
# named dollarAmount and print it.

# Given the coins shown above, the output would be 7.07 when you call calc_dollars()

def calc_dollars():
    '''calculate coins in dictionary to return dollar amount'''
    piggybank = {
            "quarters": 0,
            "dimes": 32,
            "nickles": 9,
            "pennies": 342,
        }
    for dollarAmount in piggybank.values():
        pennies = piggybank["pennies"] * .01
        dimes = piggybank["dimes"] * .1
        nickles = piggybank["nickles"] * .05
        quarters = piggybank["quarters"]
        dollarAmount = pennies + dimes + nickles
    return float(dollarAmount)
print(f"The total amount is: $",calc_dollars())


