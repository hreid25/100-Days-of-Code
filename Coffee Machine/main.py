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
    # Check only the resources required to make the drink are sufficient
    for totals_key, totals_value in menu.resources.items():
        drink_resource_cost = menu.MENU[item_ordered]['ingredients'][totals_key]
        if float(drink_resource_cost) < float(totals_value):
            # print("drink ", totals_key, " cost: ", drink_resource_cost, " available ", totals_key, " cost: ", totals_value)
            resources_sufficient = True
        elif float(drink_resource_cost) > float(totals_value):
            # print("drink ", totals_key, " cost: ", drink_resource_cost, " available ", totals_key, " cost: ", totals_value)
            resources_sufficient = False
            print(f"Sorry, there isn't enough {totals_key}.")
            break
    return resources_sufficient

def process_coins():
    coins = {'quaters':0.25, 'dimes':0.1, 'nickels':.05, 'pennies':0.01}
    coins_inserted = 0
    for key,value in coins.items():
        coin_quantity = float(input(f"How many {key}?: "))
        coins_inserted += (coin_quantity * value)
    # print(coins_inserted)
    return coins_inserted

# Asks to insert coins and quantity of each type of coin
def check_transaction(coins_inserted,drink_cost):
    # Check transaction successful
    if coins_inserted < drink_cost:
        enough_money = False
        change_to_give = 0
    elif coins_inserted >= drink_cost:
        enough_money = True
        change_to_give = (coins_inserted - drink_cost)
    return enough_money, change_to_give

# Get drink cost
def determine_item_cost(item_ordered):
    for key, value in menu.MENU.items():
        if item_ordered == key:
            drink_cost = menu.MENU[key]['cost']
    # print(key,drink_cost)
    return drink_cost

def make_coffee(item_ordered, drink_cost,change_to_give):
    # Insert money to coffers
    if 'Money' in menu.resources:
        menu.resources['Money'] += float(drink_cost)
    else:
        menu.resources['Money'] = float(drink_cost)
    # Deduct drink resources required from total resources
    for key, value in menu.MENU[item_ordered]['ingredients'].items():
        # print("current resources : " ,key, menu.resources[key], "subtract", value)
        menu.resources[key] -= value
    # Show the user that their order has been completed and present them an emoji :)
    print(f"Here is $ {change_to_give} in change.")
    print(f"Here is your {item_ordered}. Enjoy! ", emoji.emojize(":hot_beverage:"))

def main():
    order_processing = True
    while order_processing == True:
        item_ordered = input("What would you like? (espresso/latte/cappuccino)")
        # Print a report of the coffee machines resources when user types 'report'
        if item_ordered.lower() == "report":
            print(menu.resources)
        elif item_ordered.lower() == "off":
            order_processing == False
            break
        elif item_ordered == "espresso" or "latte" or "cappuccino":
            resources_sufficient = check_resources_sufficient(item_ordered)
            if resources_sufficient == True:
                # determine drink cost
                drink_cost = determine_item_cost(item_ordered)
                # add total value of coins inserted
                coins_inserted = process_coins()
                # Check that the coins inserted is at least equal to the cost of the drink and return change if necessary.
                enough_money, change_to_give = check_transaction(coins_inserted, drink_cost)
                if enough_money == True:
                    make_coffee(item_ordered, drink_cost,change_to_give)
                else:
                    print("Sorry that's not enough money. Money refunded.")
                    order_processing = False
            else:
                order_processing = False
                break
        else:
            print("That item is not on the menu. Please enter a valid option.")

main()