from classes.product import Product
from classes.order import Order
from classes.customer import Customer
from classes.discount import Discount

product1 = Product('Стул', 5500)
product2 = Product('Стол', 3800)
product3 = Product('Комод', 2300)
product4 = Product('Стеллаж', 4200)
product5 = Product('Шкаф', 12000)

discount1 = Discount('Новый клиент', 5)
discount2 = Discount('День рождения', 15)
discount3 = Discount('Распродажа', 25)
discount4 = Discount('Промокод', 10)

order1 = Order([product2, product1])
order2 = Order([product3, product4, product5], discount4)
order3 = Order([product2, product2, product2])
order4 = Order([product5, product4, product4])
order5 = Order([product3])

customer1 = Customer('Роман', [order1])
customer2 = Customer('Николай', [order2])
customer3 = Customer('Ольга', [])

print(product5)

print(discount2)

product5_discount_birthday = Discount.discount_price(product5.price, discount2.discount_percent)
print(f'Цена на {product5.name} со скидкой = {product5_discount_birthday}')

print(order2)

product1.price = product1.discount_product(discount3)
print(product1)
order6 = Order([product1])
print(order6)

order7 = Order([product5], discount1)
print(order7.total_price())
print(order7)
customer1.add_orders([order7])
customer1.add_orders([order3])
print(customer1)

customer2.add_orders([order4, order5])
print(customer2)

customer3.add_orders([order6])
print(customer3)

print('Общее количество заказов магазина: ', Order.total_orders())

all_customers = [customer1, customer2, customer3]
total = Order.all_total_price(all_customers)
print(f"Общая сумма всех заказов всех клиентов: {total}")




