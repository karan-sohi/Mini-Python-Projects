from menu import MENU, resources

def check_ingredients(coffee):
    if coffee == "expresso" or "latte" or "cappuccino":
        for item in MENU[coffee]["ingredients"]:
            if MENU[coffee]["ingredients"][item] > resources[item]:
                print(f"Not sufficient {item}")
                return False
    return True

def accept_payment():
    print("Please insert coins")
    quarters = int(input("How many quarters?: ")) * 25
    dimes = int(input("How many dimes?: ")) * 10
    nickles = int(input("How many nickles?: ")) * 5
    pennies = int(input("How many pennies?: ")) * 1
    total_cents = quarters + dimes + nickles + pennies
    total_dollars = total_cents/100
    return total_dollars

def process_payment(money, coffee):
    if MENU[coffee]["cost"] <= money:
        change = money - MENU[coffee]["cost"]
        change = round(change, 2)
        print(f"Here is your ${change} change")
        print(f"Here is your {coffee}. Enjoy!")
        return True
    else:
        print("Sorry that is not enough money. Money refunded.")
        return False


def main():
    money = 5
    user_choice = "on"
    while user_choice != "off":
        user_choice = input("What would you like? (espresso/latte/cappuccino): ")

        if user_choice == "report":
            print(f"Water: { resources['water'] } ml \nMilk: {resources['milk']}ml \nCoffee: {resources['coffee']}g \nMoney: ${money}")
        
        if user_choice == "espresso" or user_choice == "latte" or user_choice =="cappuccino":
            check_item = check_ingredients(user_choice)
            if check_item == True:
                total_money = accept_payment()
                process_payment(total_money, user_choice)

main()

    
