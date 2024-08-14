class Cooking:
    def __init__(self, cookies):
        self.cookies = cookies

    def ingredients(self):
        butter = 2.75 * self.cookies
        vanilla = 1.75 * self.cookies
        return butter, vanilla


if __name__ == "__main__":
    create = Cooking(20)
    donut = Cooking(25)
    butter_needed, vanilla_needed = create.ingredients()
    butter_donut, vanilla_donut = donut.ingredients()
    print(f"total ingredients that need to be used from {create.cookies} cookies is {butter_needed} units of butter and {vanilla_needed} units of vanilla")
    print(f"total ingredients that need to be used from {donut.cookies} cookies is {butter_donut} units of butter and {vanilla_donut} units of vanilla")
