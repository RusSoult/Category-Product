from main import Category, Product


def test_category_init():
    category = Category("Мучное", "Печенье", ["Печенье сладкое", "Печенье соленое"])
    assert category.name == "Мучное"
    assert category.characteristic == "Печенье"
    assert category.goods == ["Печенье сладкое", "Печенье соленое"]
    assert Category.count_categories == 1
    assert len(Category.products_list) == 2


def test_product_init():
    product = Product("Печенье сладкое", "Бисквитное", 138.0, 10)
    assert product.name == "Печенье сладкое"
    assert product.characteristic == "Бисквитное"
    assert product.price == 138.0
    assert product.quantity_in_stock == 10

