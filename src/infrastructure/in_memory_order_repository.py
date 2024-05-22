#from src.domain.repositories import OrderRepository
from domain.repositories import OrderRepository
from domain.entities import Order

class InMemoryOrderRepository(OrderRepository):
    def __init__(self):
        self.orders = {}
        self.current_id = 1

    def next_id(self) -> int:
        order_id = self.current_id
        self.current_id += 1
        return order_id

    def save(self, order: Order) -> None:
        self.orders[order.order_id] = order
