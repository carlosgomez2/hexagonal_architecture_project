import unittest
from src.domain.entities import Item
from src.domain.services import OrderService
from src.infrastructure.in_memory_order_repository import InMemoryOrderRepository

class TestOrderService(unittest.TestCase):
    def test_create_order(self):
        order_repository = InMemoryOrderRepository()
        order_service = OrderService(order_repository)
        items = [Item(name="item1", price=10), Item(name="item2", price=20)]
        order = order_service.create_order(items)
        self.assertEqual(order.total_price(), 30)
        self.assertEqual(order.order_id, 1)

if __name__ == "__main__":
    unittest.main()
