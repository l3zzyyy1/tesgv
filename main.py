class Product():
    def __init__(self, name, id, price):
        self.name = name
        self.id = id
        self.price = price

    def display_info(self):
        print(f"Anun: {self.name}, ID: {self.id}, Gin: {self.price}")

    def apply_discount(self):
        pass

class Electronics(Product):
    def apply_discount(self):
        self.price *= 0.9

class Clothing(Product):
    def apply_discount(self):
        self.price *= 0.8 

class Customer:
    def __init__(self):
        self.cart = []

    def add_to_cart(self, product):
        self.cart.append(product)

    def remove_from_cart(self, product):
        if product in self.cart:
            self.cart.remove(product)

    def checkout(self):
        total = 0
        for product in self.cart:
            product.apply_discount()
            total += product.price
        self.cart = []
        return total

class Shop:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)

    def search_product(self, name_or_id):
        for product in self.products:
            if product.name == name_or_id or product.id == name_or_id:
                return product
        return None

    def display_products(self):
        for product in self.products:
            product.display_info()

    def __len__(self):
        return len(self.products)

    def __str__(self):
        return f"Xanutum ka {len(self.products)} hat apranq"



shop = Shop()

laptop = Electronics("Hamakargich", "e1", 1000)
shirt = Clothing("Shor", "c1", 50)

shop.add_product(laptop)
shop.add_product(shirt)

print("Xanutum exac apranqnery:")
shop.display_products()

customer = Customer()
customer.add_to_cart(laptop)
customer.add_to_cart(shirt)

print("\nYndhanur gumary kazmum e:", customer.checkout())