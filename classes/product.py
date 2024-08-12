from classes.discount import Discount


class Product:
      
    # конструктор
    def __init__(self, name: str, price: float) -> None:
        # устанавливаем имя
        self.__name = name
        # устанавливаем цену
        self.__price = price
        
    # свойство-геттер
    @property
    def name(self):
        return self.__name
    
    # свойство-геттер
    @property
    def price(self):
        return self.__price
    
    # свойство-сеттер
    @price.setter
    def price(self, price):
        self.__price = price

    def discount_product(self, discount: Discount):
        return self.price * (1 - discount.discount_percent / 100)
       
    def __str__(self):
        return f'Название товара: {self.__name}; Цена: {self.__price}'
