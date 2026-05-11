class Ichimlik:
    def __init__(self, nom):
        self.nom = nom


class Cafe:
    def __init__(self):
        self.ichimliklar = []

    def add_drink(self, drink):
        self.ichimliklar.append(drink.nom)

    def show(self):
        print(self.ichimliklar)


i1 = Ichimlik("Cola")
i2 = Ichimlik("Fanta")

c1 = Cafe()
c1.add_drink(i1)
c1.add_drink(i2)
c1.show()
