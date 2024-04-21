class Category:
    count_categories = 0
    count_uniq_goods = 0
    products_list = []

    def __init__(self, name, characteristic, goods):
        self.name = name
        self.characteristic = characteristic
        self.goods = goods

        Category.count_categories += 1

        for good in goods:
            Category.products_list.append(good)

        Category.count_uniq_goods = len(set(Category.products_list))


class Product:
    def __init__(self, name, characteristic, price, quantity_in_stock):
        self.name = name
        self.characteristic = characteristic
        self.price = price
        self.quantity_in_stock = quantity_in_stock
