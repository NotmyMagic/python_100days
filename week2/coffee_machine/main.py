MENU = {
    "esspresso": {
        "ingrediants": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingrediants": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingrediants": {
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

cashed_money = 0


def start():
    choice = input("What drink would you like? (esspresso/latte/cappuccino) ").lower()
    if choice == "off":
        print("Goodbye")
        return
    elif choice == "report":
        for key in resources:
            print(f"{key} {resources[key]}")
        print(f"Money: ${round(cashed_money, 2)}")
        start()
    elif choice == "esspresso":
        checked_resources = get_drink(choice)
        if checked_resources == True:
            checked_cost = buy_drink(choice)
            if checked_cost == True:
                print("Here is your Esspresso. Enjoy!")
                start()
            elif checked_cost == False:
                start()
            else:
                start()
        else:
            start()

    elif choice == "latte":
        checked_resources = get_drink(choice)
        if checked_resources == True:
            checked_cost = buy_drink(choice)
            if checked_cost == True:
                print("Here is your Latte. Enjoy!")
                start()
            elif checked_cost == False:
                start()
            else:
                start()
        else:
            start()


    elif choice == "cappuccino":
        checked_resources = get_drink(choice)
        if checked_resources == True:
            checked_cost = buy_drink(choice)
            if checked_cost == True:
                print("Here is your Cappuccino. Enjoy!")
                start()
            elif checked_cost == False:
                start()
            else:
                start()
        else:
            start()

    else:
        print("Not a valid choice")
        return

def get_drink(drink_choice):
    # subtrack the cost of the drink from the machine
    for drink in MENU:
        if drink == drink_choice:
            for item in MENU[drink]["ingrediants"]:
                for key in resources:
                    if key == item:
                        resources[key] -= MENU[drink]["ingrediants"][item]
                        if int(resources[key]) < 0:
                            resources[key] += MENU[drink]["ingrediants"][item]
                            print("not enough resources")
                            return False
            return True


def buy_drink(drink_choice):
    global cashed_money
    # pennies = 0.01
    # nickles = 0.05
    # dimes = 0.1
    # quarters = 0.25
    try:
        quarters = int(input("How many quarters would you like to put in? "))
        dimes = int(input("How many dimes would you like to put in? "))
        nickles = int(input("How many nickles would you like to put in? "))
        pennies = int(input("How many pennies would you like to put in? "))

    except:
        print("Not a number please try again.")
        return

    total = 0
    for number in range(0, pennies):
        total = total + 0.01
    for number in range(0, nickles):
        total = total + 0.05
    for number in range(0, dimes):
        total = total + 0.1
    for number in range(0, quarters):
        total = total + 0.25
    total = round(total, 2)

    for drink in MENU:
        if drink == drink_choice:
            for item in MENU[drink]:
                if item == "cost":
                    if total >= MENU[drink]["cost"]:
                        total -= MENU[drink]["cost"]
                        cashed_money += MENU[drink]["cost"]
                        print(f"Your change is {total}")
                        return True
                    else:
                        print("Not enough money")
                        print("Money refunded")
                        return False

start()
