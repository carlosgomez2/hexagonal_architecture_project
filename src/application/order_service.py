from src.domain.repositories import OrderRepository

class InMemoryOrderRepository(OrderRepository):
    def __init__(self):
        self.orders = {}
        self.current_id = 1

    def next_id(self):
        order_id = self.current_id
        self.current_id += 1
        return order_id

    def save(self, order):
        self.orders[order.order_id] = order
