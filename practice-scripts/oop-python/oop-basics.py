# this will be a section for working on Object Oriented Programming OOP

class Item:
    pay_rate = 0.8
    def __init__(self, name: str, price: float, quantity=0):
        
        # instance attributes
        self.name = name
        self.price = price
        self.quantity =quantity
    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate





item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 1000, 3)
#sale attribute
item2.pay_rate = 0.7
item3 = Item("Cable", 50, 20)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

item1.apply_discount()
item2.apply_discount()

print(item1.price)
print(item2.price)