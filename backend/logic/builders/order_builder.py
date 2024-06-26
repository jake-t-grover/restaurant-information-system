from abc import ABC, abstractmethod
from ..orders.order import Order

class OrderBuilder(ABC):

    @abstractmethod
    def reset_order():
        pass

    @abstractmethod
    def add_menu_item(menu_item: dict):
        pass

    def set_customer(customer: str):
        pass

    def set_destination(customer: str):
        pass

    def get_order(location: str) -> Order:
        pass
