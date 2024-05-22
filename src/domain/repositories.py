from abc import ABC, abstractmethod
from .entities import Order

class OrderRepository(ABC):
    @abstractmethod
    def next_id(self) -> int:
        pass

    @abstractmethod
    def save(self, order: Order) -> None:
        pass
