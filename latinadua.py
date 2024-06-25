class Item:
    price_diskon = 0.8
    all = []
    def __init__(self, name: str,price: float,quantity: int = 0):
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def TotalPrice(self):
        return self.price * self.quantity
    
    def PrintItems(self):
        print(f"name = {self.name}")
        print(f"price = {self.price}")
        print(f"quantity = {self.quantity}")
        print(f"total price = {self.TotalPrice()}")
    def Diskon(self):
        print(f"diskon = {self.price * self.price_diskon}")
        self.price = self.price - (self.price * self.price_diskon)

    def __repr__(self):
        return f"{self.name}, {self.price}, {self.quantity}, {self.TotalPrice()}"
    

item1 = Item("phone", 100, 2)
item2 = Item("laptop", 300, 8)
item3 = Item("keyboard", 200, 6)

print(Item.all)

# item1.Diskon()
# item1.PrintItems()
# print("")
# item2.Diskon()
# item2.PrintItems()
# print("")
# item3.price_diskon = 0.1
# item3.Diskon()
# item3.PrintItems()