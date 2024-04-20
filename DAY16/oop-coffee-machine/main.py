from menu import Menu#, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while True:
    request = input(f"What would you like? ({menu.get_items()}): ").lower()
    if request == 'off':
        break

    elif request == 'report':
        print( f'{coffee_maker.report()}\n{money_machine.report()}')

    elif menu.find_drink(request):
        coffee = menu.find_drink(request)
        if coffee_maker.is_resource_sufficient(coffee):
        # for coffee in menu.menu:
        #     if coffee.name == request:
        #         cost = menu.menu[menu.menu.index(coffee)].cost
        #         order = menu.menu[menu.menu.index(coffee)]
            if money_machine.make_payment(coffee.cost):
                coffee_maker.make_coffee(coffee)