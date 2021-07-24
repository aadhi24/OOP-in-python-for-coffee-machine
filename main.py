from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
turns = True
while turns:

    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    menu = Menu()

    print(menu.get_items())
    choice = input("enter your coffee  ")
    if choice in "report":
        money_machine.report()
        coffee_maker.report()
    elif choice in "off":
        turns= False
    else:
        drink = menu.find_drink(choice)
        enough_ingredients = coffee_maker.is_resource_sufficient(drink)
        enough_money = money_machine.make_payment(drink.cost)
        if enough_money and enough_ingredients:
            coffee_maker.make_coffee(drink)






