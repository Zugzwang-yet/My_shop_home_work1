class Discount:

    def __init__(self, description: str, discount_percent: int):
        self.__description = description
        self.__discount_percent = discount_percent
           
    @property
    def description(self):
        return self.__description
    
    @property
    def discount_percent(self):
        return self.__discount_percent
    
    @discount_percent.setter
    def discount_percent(self, discount_percent):
        self.__discount_percent = discount_percent
        
    @staticmethod
    def discount_price(price: float, discount: int):
        return price * (1 - discount / 100)    
        
    def __str__(self):
        return f'Применяемая скидка: {self.__description}; процент скидки: {self.__discount_percent}'
    