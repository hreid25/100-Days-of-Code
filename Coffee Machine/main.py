import menu

# def print_report():
# # print the resources left, water, milk, coffee, etc.
#     print(menu.resources)

# def check_resources_sufficient():
#     # checks the order against the recipe against the drink and tells the user
#     # if resources are insufficient

def process_coins():
    coins = {'quaters':0.25, 'dimes':0.1, 'nickels':.05, 'pennies':0.01}
    coins_inserted = 0
    for key,value in coins.items():
        coin_quantity = float(input(f"How many {key}?: "))
        coins_inserted += (coin_quantity * value)
        print(coins_inserted)

    return coins_inserted

#     # asks to insert coins and quantity of each type of coin
def check_transaction(coins_inserted,item_ordered):
    # check that the input matches one of the available menu choices
    # Check transaction successful
    cost = menu[item_ordered].cost
    if coins_inserted < cost:
        print("Sorry you didn't insert enough change. Money refunded.")
    else:
        # deposit the money to the coffers and process the order



# def make_coffee():
# only runs if resources are sufficient, coins inserted > cost
#     # deduct resources from existing ingredients in menu
    #   show the user that their order has been completed and present them an emoji :)

# def main():
#     item_ordered = input("What would you like? (espresso/latte/cappucino)")
    
# main()
# process_coins()