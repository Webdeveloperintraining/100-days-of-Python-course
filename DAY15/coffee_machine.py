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
}

currency = {
    "quarter" : 0.25,
    "dime" : 0.10,
    "nickel" : 0.05,
    "penny" : 0.01,
}

def main():
    while True:
        request = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if request == 'report':
            printResources()
        elif request == 'off':
            break
        elif request in MENU:
            if not check_resources(request):
                break
            money = get_coins()
            print(f'${money}')
            coffee_cost = MENU[request]["cost"]
            if money < coffee_cost:
                print("Sorry that's not enough money. Money refunded.")
            else:
                money -= coffee_cost 
                print(f'Here is ${money} in change')
                print(f'Here is your {request.title()} ☕ Enjoy!')
                update_resources(request,coffee_cost)
                money = 0
            
def get_coins():
    print("\nPlease Insert coins: ")
    money = 0
    for i in currency:
        coin = int(input(f'How many {i}s: '))
        money += (coin * currency[i])
    return round(money,2)

def check_resources(request):
    coffe_requirements = MENU[request]['ingredients']
    for ingredient in coffe_requirements:
        coffe_ingredient = coffe_requirements[ingredient]
        resources_ingredient = resources[ingredient]
        if resources_ingredient < coffe_ingredient:
            print(f"Sorry there is not enough {ingredient}")
            return False
    return True

def printResources():
    for ingredient in resources:
        if ingredient == "milk" or ingredient == "water":
            measure = 'ml'
        else:
            measure = 'g'
        print(f'{ingredient.title()}: {resources[ingredient]}{measure}')
    print(f'Money: ${profit}')

def update_resources(request,coffee_cost):
    ingredients_used = MENU[request]['ingredients']
    for ingredient in resources:
        if ingredient not in ingredients_used:
            continue
        resources[ingredient] = (resources[ingredient] - ingredients_used[ingredient])
    global profit 
    profit += coffee_cost
main()