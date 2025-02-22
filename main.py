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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO: 1. Print a report of all the coffee machine resources


def getvalues_espresso():
    water_it_takes = MENU["espresso"]["ingredients"]["water"]
    coffee_it_takes = MENU["espresso"]["ingredients"]["coffee"]
    return water_it_takes, coffee_it_takes


def getvalues_latte():
    water_it_takes = MENU["latte"]["ingredients"]["water"]
    coffee_it_takes = MENU["latte"]["ingredients"]["coffee"]
    milk_it_takes = MENU["latte"]["ingredients"]["milk"]
    return water_it_takes, coffee_it_takes, milk_it_takes


def getvalues_cappuccino():
    water_it_takes = MENU["cappuccino"]["ingredients"]["water"]
    coffee_it_takes = MENU["cappuccino"]["ingredients"]["coffee"]
    milk_it_takes = MENU["cappuccino"]["ingredients"]["milk"]
    return water_it_takes, coffee_it_takes, milk_it_takes


def do_cost_calculation_espresso(quarters, dimes, nickles, pennies):
    """"Calculates the amount of change for an espresso"""
    quarters_ = 0.25 * quarters
    dimes_ = 0.10 * dimes
    nickles_ = 0.05 * nickles
    pennies_ = 0.01 * pennies

    money_given = quarters_ + dimes_ + nickles_ + pennies_
    cost = MENU["espresso"]["cost"]

    change = money_given - cost
    return round(change, 2), round(money_given, 2)


def do_cost_calculation_latte(quarters, dimes, nickles, pennies):
    """"Calculates the amount of change for a latte"""
    quarters_ = 0.25 * quarters
    dimes_ = 0.10 * dimes
    nickles_ = 0.05 * nickles
    pennies_ = 0.01 * pennies

    money_given = quarters_ + dimes_ + nickles_ + pennies_
    cost = MENU["latte"]["cost"]

    change = money_given - cost
    return round(change, 2), round(money_given, 2)


def do_cost_calculation_cappuccino(quarters, dimes, nickles, pennies):
    """"Calculates the amount of change for a cappuccino"""
    quarters_ = 0.25 * quarters
    dimes_ = 0.10 * dimes
    nickles_ = 0.05 * nickles
    pennies_ = 0.01 * pennies

    money_given = quarters_ + dimes_ + nickles_ + pennies_
    cost = MENU["cappuccino"]["cost"]

    change = money_given - cost
    return round(change, 2), round(money_given, 2)


loop = True
water_resource = resources["water"]
coffee_resource = resources["coffee"]
milk_resource = resources["milk"]
money = 0

while loop:
    question = input("What would you like? (espresso/latte/cappuccino): ")

    if question == "report":
        # Loop through the dictionary resources to print the amount of resources left
        for key, value in zip(resources.keys(), resources.values()):
            print(f"{key}: {value}")
        print(f"Money: ${money}")

    elif question == "espresso":

        quarters = float(input("How many Quarters? "))
        dimes = float(input("How many Dimes? "))
        nickles = float(input("How many nickles? "))
        pennies = float(input("How many pennies? "))

        water_it_takes, coffee_it_takes = getvalues_espresso()
        
        # ✅ Check if there are enough resources before proceeding
        if water_it_takes > resources["water"]:
            print("Sorry, not enough water.")
        elif coffee_it_takes > resources["coffee"]:
            print("Sorry, not enough coffee.")
        else:
            change, money_given = do_cost_calculation_espresso(quarters, dimes, nickles, pennies)

            if change < 0:
                print("Sorry that's not enough money. Money refunded.")
            else:
                resources["water"] -= water_it_takes
                resources["coffee"] -= coffee_it_takes
                money += money_given

                print(f"Here is ${change} change")
                print("Here is your espresso ☕ enjoy")

    elif question == "latte":
        quarters = float(input("How many Quarters? "))
        dimes = float(input("How many Dimes? "))
        nickles = float(input("How many nickles? "))
        pennies = float(input("How many pennies? "))

        water_it_takes, coffee_it_takes, milk_it_takes = getvalues_latte()

        # ✅ Check if there are enough resources before proceeding
        if water_it_takes > resources["water"]:
            print("Sorry, not enough water.")
        elif coffee_it_takes > resources["coffee"]:
            print("Sorry, not enough coffee.")
        elif milk_it_takes > resources["milk"]:
            print("Sorry, not enough milk.")
        else:
            change, money_given = do_cost_calculation_latte(quarters, dimes, nickles, pennies)

            if change < 0:
                print("Sorry that's not enough money. Money refunded.")
            else:
                resources["water"] -= water_it_takes
                resources["coffee"] -= coffee_it_takes
                resources["milk"] -= milk_it_takes
                money += money_given

                print(f"Here is ${change} change")
                print("Here is your latte ☕ enjoy")

    elif question == "cappuccino":
        quarters = float(input("How many Quarters? "))
        dimes = float(input("How many Dimes? "))
        nickles = float(input("How many nickles? "))
        pennies = float(input("How many pennies? "))

        water_it_takes, coffee_it_takes, milk_it_takes = getvalues_cappuccino()

        # ✅ Check if there are enough resources before proceeding
        if water_it_takes > resources["water"]:
            print("Sorry, not enough water.")
        elif coffee_it_takes > resources["coffee"]:
            print("Sorry, not enough coffee.")
        elif milk_it_takes > resources["milk"]:
            print("Sorry, not enough milk.")
        else:
            change, money_given = do_cost_calculation_cappuccino(quarters, dimes, nickles, pennies)

            if change < 0:
                print("Sorry that's not enough money. Money refunded.")
            else:
                resources["water"] -= water_it_takes
                resources["coffee"] -= coffee_it_takes
                resources["milk"] -= milk_it_takes
                money += money_given

                print(f"Here is ${change} change")
                print("Here is your cappuccino ☕ enjoy")

    elif question == "off":
        print("Computer shut down")
        loop = False
