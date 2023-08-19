"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        assert product.check_quantity(product.quantity-1)
        assert product.check_quantity(product.quantity)
        assert not product.check_quantity(product.quantity+1), (f"Недостаточное количество {product.name} на складе. "
                                                                f"Максмальное количество {product.quantity} шт.")
        # TODO напишите проверки на метод check_quantity

    def test_product_buy(self, product):
        buying_quantity = 1
        product_quantity_before_sell = product.quantity
        remaining_quantity = product.buy(buying_quantity)
        assert remaining_quantity == product_quantity_before_sell - buying_quantity
        # TODO напишите проверки на метод buy

    def test_product_buy_more_than_available(self, product):
        buying_quantity = product.quantity+1
        try:
            product.buy(buying_quantity)
        except ValueError:
            return True
        else:
            assert False #не придумал как нормально уронить тест, return False не сработал

        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии



class TestCart:
    cart = Cart
    def test_add_product(self, product):
        Cart
        # cart.add_product(productk)
        # assert product in cart.products


    # def add_product(self, product: Product, buy_count=1):
    #     if not self.products.get(product):
    #         self.products.update(product=buy_count)
    #     else:
    #         self.products.update(product=self.products.get(product) + buy_count)
    #     return self.products
    #     """
    #     Метод добавления продукта в корзину.
    #     Если продукт уже есть в корзине, то увеличиваем количество
    #     """
    #     raise NotImplementedError
    #
    # def remove_product(self, product: Product, remove_count=None):
    #     """
    #     Метод удаления продукта из корзины.
    #     Если remove_count не передан, то удаляется вся позиция
    #     Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция
    #     """
    #     raise NotImplementedError
    #
    # def clear(self):
    #     raise NotImplementedError
    #
    # def get_total_price(self) -> float:
    #     raise NotImplementedError
    #
    # def buy(self):

    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
