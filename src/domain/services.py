from .entities import Order, Item
from .repositories import OrderRepository

class OrderService:
    def __init__(self, order_repository: OrderRepository):
        self.order_repository = order_repository

    def create_order(self, items: list[Item]) -> Order:
        order = Order(order_id=self.order_repository.next_id(), items=items)
        self.order_repository.save(order)
        return order
