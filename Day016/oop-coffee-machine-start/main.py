from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create objects from imported classes
my_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()

# Print Resources

is_on = True
while is_on:
    #  Prompt user by asking, "What would you like? (espresso/latte/cappuccino): "
    user_choice = input(f"What would you like? {my_menu.get_items()}: \n"
                        "Type 'off' to exit \n"
                        "Or 'report to check the resources \n>").lower()
    # Turn off the coffee machine by entering "off" to the prompt
    if user_choice == "off":
        is_on = False

    # Print report of resources
    elif user_choice == "report":
        my_coffee_maker.report()
        my_money_machine.report()

    # Check if the drink is available
    else:
        drink = my_menu.find_drink(user_choice)
        if drink is not None:
            if my_coffee_maker.is_resource_sufficient(drink):
                if my_money_machine.make_payment(drink.cost):
                    my_coffee_maker.make_coffee(drink)
                    print("* * * * * * * * * * ")
                    print("\n")
        else:
            print("Sorry, that item is not available.")
