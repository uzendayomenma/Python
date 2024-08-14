from Recipe import *


class BakeIt(Cooking):
    def __init__(self, cookies, baking_time=0):
        super().__init__(cookies)
        self.all = []
        self.baking_time = baking_time
        self.add_cookies()

    def add_cookies(self):
        self.all.append(self.cookies)

    def get_cookies(self):
        return self.all

    def show_if_its_cook(self):
        if self.baking_time < 10:
            return False
        return True


if __name__ == "__main_ _":
    Bakery = BakeIt(5, 10)
    Bakery1 = BakeIt(9, 10)

    print(Bakery.show_if_its_cook())
    print(Bakery.get_cookies())
    print(Bakery1.show_if_its_cook())
    print(Bakery1.get_cookies())
