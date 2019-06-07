class Product:
    def __init__(self, name, price, stock=0, discount=0, max_discount=20):
        self.name = name.strip()
        if len(self.name) < 2:
            raise ValueError('too short, extend it')
        self.price = abs(float(price))
        self.stock = abs(int(stock))
        self.discount = abs(float(discount))
        self.max_discount = abs(float(max_discount))
        if self.max_discount > 99:
            raise ValueError('do not lead a dance')
        if self.discount > self.max_discount:
            self.discount = self.max_discount

    def discounted(self):
        return self.price - self.price * self.discount / 100

    def sell(self, items_count=1):
        if items_count > self.stock:
            raise ValueError('not enough')
        self.stock -= items_count
    
    def get_colour(self):
        raise NotImplementedError

    
    def __repr__(self):
        return f'<product name: {self.name}, price: {self.price}, stock: {self.stock}>'

class Phone(Product):
    def __init__(self, name, price, colour, stock=0, discount=0, max_discount=20):
        super().__init__(name, price, stock, discount, max_discount)
        self.colour = colour
    
    def get_colour(self):
        return f'case colour: {self.colour}'

    def __repr__(self):
        return f'<phone name: {self.name}, price: {self.price}, stock: {self.stock}>'

class Sofa(Product):
    def __init__(self, name, price, colour, texture, discount=0, stock=0, max_discount=20.0):
        super().__init__(name, price, discount, stock, max_discount)
        self.colour = colour
        self.texture = texture

    def __repr__(self):
        return f'<Sofa name: {self.name}, price: {self.price}, stock: {self.stock}>'

product1 = Product('pills', 122, stock=22)
product1.sell(3)
print(product1)

phone1 = Phone('iphone7', 700, 'черный')
print(phone1)
print(phone1.colour)
print(phone1.get_colour())

sofa1 = Sofa('cozysofa', 300, 'green', 'silk')
print(sofa1)
print(sofa1.texture)
print(sofa1.get_colour())