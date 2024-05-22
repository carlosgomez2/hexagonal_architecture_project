class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self, order_id, items):
        self.order_id = order_id
        self.items = items

    def total_price(self):
        return sum(item.price for item in self.items)
