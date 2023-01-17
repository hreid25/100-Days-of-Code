import menu
import emoji

def print_report():
# print the resources left, water, milk, coffee, etc.
    for key, value in menu.resources.items():
        if key == "water" or key == "milk":
            std_measure = "ml"
        elif key == "coffee":
            std_measure = "g"
        # elif key == "Money": 
        # Need to print out the total Money accrued so far.
        print(str(key.title()),": ", value, std_measure)

# Turn off the machine by entering 'off' to the prompt
# def turn_off_machine():

def check_resources_sufficient(item_ordered):
    # deduct resources from existing ingredients in menu
    for key, value in menu.MENU.items():
        if item_ordered == key:
            # Collect total water, milk and coffee cost of drink
            for key, value in menu.MENU[item_ordered]['ingredients'].items():
                for totals_key, totals_value in menu.resources.items():
                    if key == totals_key:
                        if value < totals_value:
                            # print("latte cost: ", value, "resources: ", totals_value)
                            resources_sufficient = True
                        elif value >= totals_value:
                            # print("latte cost: ", value, "resources: ", totals_value)
                            resources_sufficient = False
    return resources_sufficient
            # for key, value in
            # Subtract the water, milk and coffee total from the resources dict

def process_coins():
    coins = {'quaters':0.25, 'dimes':0.1, 'nickels':.05, 'pennies':0.01}
    coins_inserted = 0
    for key,value in coins.items():
        coin_quantity = float(input(f"How many {key}?: "))
        coins_inserted += (coin_quantity * value)
    print(coins_inserted)
    return coins_inserted

# Asks to insert coins and quantity of each type of coin
def check_transaction(coins_inserted,drink_cost):
    # Check transaction successful
    if coins_inserted < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
    elif coins_inserted > drink_cost:
        # Return change
        change_to_give = (coins_inserted - drink_cost)
    return change_to_give

# Get drink cost
def determine_item_cost(item_ordered):
    for key, value in menu.MENU.items():
        if item_ordered == key:
            drink_cost = menu.MENU[key]['cost']
    print(key,drink_cost)
    return drink_cost

def make_coffee(item_ordered, drink_cost,change_to_give):
    # Insert money to coffers
    menu.resources['Money'] += drink_cost
    # Deduct drink resources required from total resources
    for key, value in menu.resources.items():
        if key == item_ordered:
            key[value] -= menu.MENU[key]['ingredient']
    # Show the user that their order has been completed and present them an emoji :)
    print(f"Here is $ {change_to_give} in change.")
    print(f"Here is your {item_ordered} ", emoji.emojize(":hot_beverage:"))

def main():
    order_processing = True
    while order_processing == True:
        item_ordered = input("What would you like? (espresso/latte/cappucino)")
        # Print a report of the coffee machines resources when user types 'report'
        if item_ordered == "Report":
            print(menu.resources)
        # determine drink cost
        drink_cost = determine_item_cost(item_ordered)
        # add total value of coins inserted
        coins_inserted = process_coins()
        # Check that the coins inserted is at least equal to the cost of the drink and return change if necessary.
        change_to_give = check_transaction(coins_inserted, drink_cost)
        if change_to_give is None:
            order_processing = False
            break
        else:
            resources_sufficient = check_resources_sufficient(item_ordered)
            if resources_sufficient == True:
                make_coffee(item_ordered, drink_cost,change_to_give)
            else:
                order_processing = False
                break

main()