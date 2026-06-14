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
    "profit": 0
}
user_input=str(input("what would you like? espresso, latte, cappuccino, off, report ")).lower()
def currency_counter():

    print(f"cost is {MENU[user_input]['cost']}")
    q=int(input("₹quarter"))*0.25
    d=int(input("₹dime"))*0.1
    n=int(input("₹nickel"))*0.05
    p=int(input("₹penny"))*0.01
    sum_m=q+d+n+p
    print(f"you gave ₹{sum_m}")
    if sum_m<MENU[user_input]["cost"]:
        print("you don't have enough money")
    elif sum_m>MENU[user_input]["cost"]:
        extra=sum_m -MENU[user_input]["cost"]
        print(f" refund ₹{extra} ")
        resources["profit"] += MENU[user_input]["cost"]
    else:
        resources["profit"]+=MENU[user_input]["cost"]


while user_input in ["espresso", "latte", "cappuccino", "off", "report"]:
    if user_input == "off":
        break
    elif user_input == "report":
        print(resources)
        print("\n")
    elif user_input=="espresso":
        if resources["water"] <50 or resources["coffee"] <18:
            print(f"sorry not enough resources{resources}\n")
            break
        else:
            currency_counter()
            resources["water"]-=MENU[user_input]["ingredients"]["water"]
            #resources["milk"]-=MENU[user_input]["ingredients"]["milk"]
            resources["coffee"]-=MENU[user_input]["ingredients"]["coffee"]
            print(f"order taken: {user_input}\n")
    elif user_input=="latte":
        if resources["water"] <200 or resources["milk"] <150 or resources["coffee"] <24:
            print(f"sorry not enough resources{resources}\n")
            break
        else:
            currency_counter()
            resources["water"]-=MENU[user_input]["ingredients"]["water"]
            resources["coffee"]-=MENU[user_input]["ingredients"]["coffee"]
            resources["milk"]-=MENU[user_input]["ingredients"]["milk"]
            print(f"order taken: {user_input}\n")
    else:
        if resources["water"] <250 or resources["milk"] <100 or resources["coffee"] <24:
            print(f"sorry not enough resources{resources}\n")
            break
        else:
            currency_counter()
            resources["water"] -= MENU[user_input]["ingredients"]["water"]
            resources["coffee"] -= MENU[user_input]["ingredients"]["coffee"]
            resources["milk"] -= MENU[user_input]["ingredients"]["milk"]
            print(f"order taken: {user_input}\n")

    user_input=str(input("what would you like? espresso, latte, cappuccino, off, report ")).lower()
