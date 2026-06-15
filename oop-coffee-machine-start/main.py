from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffe = CoffeeMaker()
money_machine = MoneyMachine()
coffe.report()
money_machine.report()
menu=Menu()



order=True
while order:
    user_order = str(input(f"enter your order{menu.get_items()}, report, off: "))
    menu_item = menu.find_drink(user_order)
    if user_order in menu.get_items():
        if coffe.is_resource_sufficient(menu_item):
            print(f"your  {user_order} is {menu_item.cost: }")
            money_machine.make_payment(menu_item.cost)
            coffe.make_coffee(menu_item)
            coffe.report()

        else:
            break



    elif user_order == "report":
        money_machine.report()
        coffe.report()
    elif user_order == "off":
        order=False

