from domain.entities import Item
from domain.services import OrderService
from infrastructure.in_memory_order_repository import InMemoryOrderRepository

def main():
    order_repository = InMemoryOrderRepository()
    order_service = OrderService(order_repository)

    items = [Item(name="item1", price=10), Item(name="item2", price=20)]
    order = order_service.create_order(items)
    print(f"Order created with ID: {order.order_id} and total price: {order.total_price()}")

if __name__ == "__main__":
    main()
