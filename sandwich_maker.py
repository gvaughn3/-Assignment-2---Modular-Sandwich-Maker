class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        for item in ingredients:
            if self.machine_resources.get(item, 0) < ingredients[item]:
                print("Insufficient ingredients")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item]
        print(f"{sandwich_size} sandwich is ready. Bon appetit!")

    def report(self):
        print(f"Bread: {self.machine_resources['bread']} slice(s)")
        print(f"Ham: {self.machine_resources['ham']} slice(s)")
        print(f"Cheese: {self.machine_resources['cheese']} ounces")