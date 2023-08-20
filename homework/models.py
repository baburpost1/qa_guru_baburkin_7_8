class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity) -> bool:
        if quantity > 0 and self.quantity >= quantity:
            return True
        else:
            return False

        """
        TODO Верните True если количество продукта больше или равно запрашиваемому
            и False в обратном случае
        """

    def buy(self, quantity):
        if self.check_quantity(quantity):
            self.quantity = self.quantity - quantity
            return self.quantity
        else:
            raise ValueError(f"Недостаточное количество {self.name} на складе. "
                             f"Максмальное количество {self.quantity} шт.")
        """
        TODO реализуйте метод покупки
            Проверьте количество продукта используя метод check_quantity
            Если продуктов не хватает, то выбросите исключение ValueError
        """

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
        if not self.products.get(product):
            product_name = product.name
            self.products[product] = buy_count
        else:
            self.products[product] = self.products.get(product) + buy_count
        return self.products
        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """

    def remove_product(self, product: Product, remove_count=None):
        if remove_count == None or remove_count > self.products.get(product):
            self.products.pop(product)
        else:
            self.products[product] = self.products.get(product) - remove_count
        """
        Метод удаления продукта из корзины.
        Если remove_count не передан, то удаляется вся позиция
        Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция
        """

    def clear(self):
        self.products.clear()

    def get_total_price(self) -> float:
        total_price = 0
        for product in self.products:
            total_price = product.price * self.products.get(product)
        return total_price

    def buy(self):
        """
        Если количества товара на складе хватает, то он списывается на величину указанную в корзине и удаляется из неё
        Если количества товара на складе НЕ хватает, то товар остаётся в корзине, списание со склада не происходит
        """
        product_not_enough_quantity = {}
        for product in self.products:
            if not product.check_quantity(self.products.get(product)):
                product_not_enough_quantity[product] = self.products.get(product)
            else:
                product.quantity = product.quantity - self.products.get(product)
        self.products.clear()
        # Если нужно вернуть просто ValueError, то понятно, что не нужно возвращать словарь с продуктами
        if len(product_not_enough_quantity) > 0:
            raise ValueError
        else:
            return product_not_enough_quantity

        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """
