class Category:
    count_categories = 0
    count_goods = set()
    count_products = []

    def __init__(self, name, characteristic, goods):
        self.name = name
        self.characteristic = characteristic
        self.goods = goods

        Category.count_categories += 1
        Category.count_goods.update(goods)

        for good in goods:
            Category.count_products.append(good)


class Product:
    def __init__(self, name, characteristic, price, quantity_in_stock):
        self.name = name
        self.characteristic = characteristic
        self.price = price
        self.quantity_in_stock = quantity_in_stock
