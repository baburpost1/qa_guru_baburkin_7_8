from dataclasses import dataclass


@dataclass
class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int

    def check_quantity(self, quantity) -> bool:
        """
        TODO Верните True если количество продукта больше или равно запрашиваемому
            и False в обратном случае
        """
        if 0 < quantity <= self.quantity:
            return True
        else:
            return False

    def buy(self, quantity):
        """
        TODO реализуйте метод покупки
            Проверьте количество продукта используя метод check_quantity
            Если продуктов не хватает, то выбросите исключение ValueError
        """
        if self.check_quantity(quantity):
            self.quantity = self.quantity - quantity
            return self.quantity
        else:
            raise ValueError(f"Недостаточное количество {self.name} на складе. "
                             f"Максмальное количество {self.quantity} шт.")

    def __hash__(self):
        return hash(self.name + self.description)


class Cart:
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    TODO реализуйте все методы класса
    """

    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    def add_product(self, product: Product, buy_count=1):
        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """
        if not self.products.get(product):
            self.products[product] = buy_count
        else:
            self.products[product] = self.products.get(product) + buy_count
        return self.products

    def remove_product(self, product: Product, remove_count=None):
        """
        Метод удаления продукта из корзины.
        Если remove_count не передан, то удаляется вся позиция
        Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция
        """
        if remove_count is None or remove_count > self.products.get(product):
            self.products.pop(product)
        else:
            self.products[product] = self.products.get(product) - remove_count

    def clear(self):
        self.products.clear()

    def get_total_price(self) -> float:
        total_price = 0
        for product in self.products:
            total_price = product.price * self.products.get(product)
        return total_price

    def buy(self):
        """
        TODO: Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """
        """
        Если количества товара на складе хватает, то он списывается на величину указанную в корзине и удаляется из неё
        Если количества товара на складе НЕ хватает, то товар остаётся в корзине, списание со склада не происходит
        """
        product_not_enough_quantity = {}
        for product in self.products:
            product.buy(self.products.get(product))
        self.products.clear()
        # Если нужно вернуть просто ValueError, то понятно, что не нужно возвращать словарь с продуктами
        if len(product_not_enough_quantity) > 0:
            raise ValueError
        else:
            return product_not_enough_quantity
