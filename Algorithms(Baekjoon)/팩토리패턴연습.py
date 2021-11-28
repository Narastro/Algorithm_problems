from abc import ABCMeta, abstractmethod


class Pizza(ABCMeta):
    def __init__(self):
        self.topping = 1

    @abstractmethod
    def addTopping(self):
        self.topping += 1


class SweetPotato(Pizza):
    def __init__(self):
        super().__init__()
        self.name = 'sweet potato'


class Potato(Pizza):
    def __init__(self):
        super().__init__()
        self.name = 'potato'


class Peperoni(Pizza):
    def __init__(self):
        super().__init__()
        self.name = 'peperoni'


class PizzaFactory:
    def createPizza(pizzaType: str):
        if pizzaType == 'sweet potato':
            return SweetPotato()

        if pizzaType == 'potato':
            return Potato()

        if pizzaType == 'peperoni':
            return Peperoni()

        return None


peperoni = Peperoni()
print(peperoni.name)
print(peperoni.topping)
