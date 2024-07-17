class Dealership:
    discount = 0.7
    all = []
    buyer = ""

    def __init__(self, car, price: float, year_model: int):
        if not isinstance(car, str) and (price, float):
            raise ValueError("Wrong type format")
        self.car = car
        self.price = price
        self.model = year_model

        Dealership.all.append(self)

    def showcase(self):
        print(f"{self.car}, ${self.price}, {self.model} model")

    def apply_discount(self):
        self.price = self.price * self.discount

    def __repr__(self):
        return (f"({self.car},"
                f" {self.price},"
                f" {self.model})")

    @classmethod
    def set_discount(cls, amount):
        cls.discount = amount
        return cls.discount

    @classmethod
    def view_all(cls):
        return cls.all

    @classmethod
    def unit_buyer(cls, buyer):
        cls.buyer = buyer
        return cls.buyer

    @staticmethod
    def set_id(id1):
        return id1


Unit1 = Dealership("Toyota", 20000, 2008)
Unit2 = Dealership("Supra", 1000000, 2024)

print(Dealership.set_id(51231))