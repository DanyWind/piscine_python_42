from beverages import HotBeverage, Coffee
import random

class BrokenMachineException(Exception):
    "This coffee machine has to be repaired"
    pass

class EmptyCup(HotBeverage):
    @property
    def description(self):
        return "An empty cup?! Gimme my money back!"

    def __init__(self):
        super().__init__("empty cup",0.9)

class CoffeeMachine:
    def serve(self,BeverageClass):
        if self.broken:
            raise BrokenMachineException

        rand = random.random()
        if rand > 0.5:
            # Machine broke
            output = EmptyCup()
        else:
            output = BeverageClass()

        self.n_cup += 1

        if self.n_cup == 10:
            self.broken = True

        return output

    def repair(self):
        self.n_cup = 0
        self.broken = False

    def __init__(self):
        self.n_cup = 0
        self.broken = False

if __name__ == "__main__":
    cm = CoffeeMachine()

    n = 30
    for i in range(n):
        try:
            hot_beverage = cm.serve(Coffee)
        except BrokenMachineException:
            print("Machine broke, repairing ...")
            cm.repair()
            hot_beverage = cm.serve(Coffee)
        print(hot_beverage)