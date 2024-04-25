# Coffee Machine

# Makes 3 hot flavors of coffee: espresso, latte, and cappuccino
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0

resources = {
    "water": 3000,
    "milk": 2000,
    "coffee": 1000,
    "money": 0
}

# Coins Operated
coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01
}


def is_resource_sufficient(order_ingredients):
    """
    Returns True when order can be made,
    False if ingredients are insufficient
    """
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_coins():
    """
    Returns the total calculated from coins inserted
    """
    print("Please insert coins.")
    total = int(input("How many quarters? ")) * coins["quarters"]
    total += int(input("How many dimes? ")) * coins["dimes"]
    total += int(input("How many nickels? ")) * coins["nickels"]
    total += int(input("How many pennies? ")) * coins["pennies"]
    return total


def is_transaction_successful(money_received, drink_cost):
    """
    Return True when the payment is accepted, or False if money is insufficient
    """
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """
    Deduct the required ingredients from the resources
    """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True
while is_on:
    #  Prompt user by asking, "What would you like? (espresso/latte/cappuccino): "
    user_choice = input("What would you like? (espresso/latte/cappuccino)? \n"
                        "Type 'off' to exit, or 'reports' to make a report \n").lower()
    # Turn off the coffee machine by entering "off" to the prompt
    if user_choice == "off":
        is_on = False
    # Print report of resources
    elif user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
    else:
        drink = MENU[user_choice]
        if is_resource_sufficient(drink["ingredients"]):
            # Process coins
            payment = process_coins()
            # Check transaction successful
            if is_transaction_successful(payment, drink["cost"]):
                # Make coffee
                make_coffee(user_choice, drink["ingredients"])
                # Deduct resources
                resources["money"] += drink["cost"]
                # Give change

            else:
                print("Sorry, not enough resources")
        else:
            print("Sorry, not enough resources")
