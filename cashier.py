class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        print("Insert coins:")
        dollars = int(input("How many dollars?: "))
        half_dollars = int(input("How many half dollars?: "))
        quarters = int(input("How many quarters?: "))
        nickels = int(input("How many nickels?: "))
        total = (dollars * 1.0) + (half_dollars * 0.5) + (quarters * 0.25) + (nickels * 0.05)
        return total

    def transaction_result(self, coins, cost):
        if coins < cost:
            print("Insufficient amount, money refunded")
            return False
        change = round(coins - cost, 2)
        print(f"Here is ${change} in change")
        return True