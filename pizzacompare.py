class Pizzatest:
    def __init__(self, pizza1, pizza2):

        self.pizza1 = pizza1
        self.pizza2 = pizza2
        self.final = ""
        self.test()

    def test(self):
        pizza1price = 0
        pizza2price = 0
        if self.pizza1 == "PapaJohns":
            pizza1price = 13
        if self.pizza1 == "Dominos":
            pizza1price = 8
        if self.pizza1 == "LittleCaesars":
            pizza1price = 6
        if self.pizza1 == "PizzaHut":
            pizza1price = 12

        if self.pizza2 == "PapaJohns":
            pizza2price = 13
        if self.pizza2 == "Dominos":
            pizza2price = 8
        if self.pizza2 == "LittleCaesars":
            pizza2price = 6
        if self.pizza2 == "PizzaHut":
            pizza2price = 12

        if pizza1price > pizza2price:
            self.final = self.pizza1 + " is more expensive than " + self.pizza2
        if pizza1price < pizza2price:
            self.final = self.pizza2 + " is more expensive than " + self.pizza1
        if pizza1price == pizza2price:
            self.final = "That's the same pizza place silly."


    @property
    def endgame(self):
        return self.final

if __name__ == "__main__":
    pizzatest = Pizzatest("Dominos", "LittleCaesars")
    print(pizzatest.endgame)