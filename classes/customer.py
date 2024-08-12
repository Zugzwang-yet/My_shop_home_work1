from classes.order import Order

class Customer:

    # конструктор
    def __init__(self, name: str, orders: list[Order]):
        # задаем имя
        self.__name = name
        # задаем список покупок
        self.__orders = orders
        
    # свойство-геттер
    @property
    def name(self):
        return self.__name
    
    # свойство-геттер
    @property
    def orders(self):
        return self.__orders
        
    # свойство-сеттер
    @orders.setter
    def orders(self, orders):
        self.__orders = orders
        
    def add_orders(self, other: list):
        return self.orders.extend(other)
  
    def all_orders(self):
        return len(self.orders)
    
    def all_price(self):
        return sum(order.total_price() for order in self.orders)
                    
    def __str__(self):
        return f'Имя клиента: {self.__name}; Количество заказов клиента: {self.all_orders()}; Общая сумма заказов клиента: {self.all_price()}'
    
    