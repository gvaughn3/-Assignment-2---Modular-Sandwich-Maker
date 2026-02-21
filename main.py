import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

def main():
    resources = data.resources
    recipes = data.recipes

    sandwich_maker_instance = SandwichMaker(resources)
    cashier_instance = Cashier()

    is_on = True
    while is_on:
        choice = input("What would you like? (small/ medium/ large/ off/ report): ").strip().lower()

        if choice == "off":
            is_on = False

        elif choice == "report":
            sandwich_maker_instance.report()

        elif choice in recipes:
            order_ingredients = recipes[choice]["ingredients"]
            cost = recipes[choice]["cost"]

            if sandwich_maker_instance.check_resources(order_ingredients):
                coins = cashier_instance.process_coins()
                if cashier_instance.transaction_result(coins, cost):
                    sandwich_maker_instance.make_sandwich(choice, order_ingredients)

        else:
            pass

if __name__ == "__main__":
    main()