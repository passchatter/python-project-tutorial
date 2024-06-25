class Item:

    pay_rate = 0.8
    all = []
    def __init__(self, nama: str, price: float, quantity: int = 0):

        assert quantity >= 0,f"quantity {quantity} is not greater than or equal to zero!"
        assert price >= 0, f"price {price} is not greater than or equal to zero!"

        self.nam = nama
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def Calculate_total(self):
        return self.price * self.quantity
    
    def PrintHasil(self):
        print(f"nama = {self.nam}")
        print(f"price = {self.price}")
        print(f"quantity = {self.quantity}")
        print(f"jumlah = {self.Calculate_total()}")

    def Diskon(self):
        self.price = self.price - (self.price * self.pay_rate)
      
    def __repr__(self):
        return f"iten({self.nam}, {self.price}, {self.quantity}, {self.Calculate_total()})"

item1 = Item("phone", 100, 1)
item2 = Item("laptop", 1000, 3)

print(Item.all)



