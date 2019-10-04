class HotBeverage:
    @property
    def description(self):
        return "Just some hot water in a cup."

    def __init__(self,name=None,price=None):
        self.name = "coffee" if not name else name
        self.price = 0.4 if not price else price

    def __str__(self):
        output = []
        output.append(f"name : {self.name}")
        output.append(f"price : {self.price}")
        output.append(f"description : {self.description}")
        output = "\n".join(output)
        return output

class Coffee(HotBeverage):
    @property
    def description(self):
        return "A coffee, to stay awake"

    def __init__(self):
        super().__init__(name="coffee")

class Chocolate(HotBeverage):
    @property
    def description(self):
        return "Chocolate, sweet chocolate"

    def __init__(self):
        super().__init__("chocolate",0.5)

class Cappucino(HotBeverage):
    @property
    def description(self):
        return "Un po’ di Italia nella sua tazza!"

    def __init__(self):
        super().__init__("cappucino",0.45)

class Tea(HotBeverage):
    def __init__(self):
        super().__init__(name="tea",price=0.3)

if __name__ == "__main__":
    beverages = [
        HotBeverage(),
        Coffee(),
        Cappucino(),
        Chocolate(),
        Tea()
    ]
    for b in beverages:
        print(b)