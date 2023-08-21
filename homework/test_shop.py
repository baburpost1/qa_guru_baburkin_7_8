"""
Протестируйте классы из модуля homework/models.py
"""
import pytest
from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture()
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(product.quantity - 1)
        assert product.check_quantity(product.quantity)
        assert not product.check_quantity(product.quantity + 1), (f"Недостаточное количество {product.name} на складе. "
                                                                  f"Максмальное количество {product.quantity} шт.")

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        buying_quantity = 1
        product_quantity_before_sell = product.quantity
        remaining_quantity = product.buy(buying_quantity)
        assert remaining_quantity == product_quantity_before_sell - buying_quantity

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        buying_quantity = product.quantity + 1
        with pytest.raises(ValueError):
            product.buy(buying_quantity)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, product, cart):
        cart.add_product(product)
        assert product in cart.products
        cart.add_product(product, buy_count=2)
        assert cart.products.get(product) == 3
        assert cart.products.__len__() == 1

    def test_remove_product_wo_remove_count(self, product, cart):
        cart.add_product(product, buy_count=3)
        cart.remove_product(product)
        assert product not in cart.products

    def test_remove_product_remove_count_more_then_quantity(self, product, cart):
        cart.add_product(product, buy_count=1)
        cart.remove_product(product, remove_count=2)
        assert product not in cart.products

    def test_remove_product_from_empty_cart(self, product, cart):
        with pytest.raises(KeyError):
            cart.remove_product(product)

    def test_clear_cart(self, product, cart):
        cart.add_product(product)
        cart.clear()
        assert len(cart.products) == 0, f"После очистки в корзине остался товар: {product.name}"

    def test_total_price(self, product, cart):
        cart.add_product(product, buy_count=3)
        total_price = 3 * product.price
        assert total_price == cart.get_total_price()

    def test_buy_enough_quantity(self, product, cart):
        cart.add_product(product, product.quantity - 1)
        products_not_enough_quantity = cart.buy()
        assert len(products_not_enough_quantity) == 0
        assert product.quantity == 1

    def test_buy_not_enough_quantity(self, product, cart):

        cart.add_product(product, product.quantity + 1)
        with pytest.raises(ValueError):
            cart.buy()
