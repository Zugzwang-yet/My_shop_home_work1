from classes.discount import Discount
from classes.product import Product

class Order:
    _total_orders = 0
    
    def __init__(self, products: list[Product], discount: Discount = None):
        self.products = products
        self.discount = discount
        Order._total_orders += 1
        
    @classmethod
    def total_orders(cls):
        return cls._total_orders
    
    def total_price(self):
        if self.discount:
            return sum(product.discount_product(self.discount) for product in self.products)
        return sum(product.price for product in self.products)
    
    @classmethod
    def all_total_price(cls, customers: list):
        return sum(customer.all_price() for customer in customers)
        
    def __str__(self):
        return f'Сумма заказа = {self.total_price()}'
