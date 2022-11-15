class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def in_stock(self, quantity):
        return self.quantity >= quantity
