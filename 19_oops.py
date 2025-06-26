# E-commerce Cart

# Create a Product class with attributes name, price, and quantity.
# Implement a ShoppingCart class to add, remove, and view products in the cart.


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - ${self.price} x {self.quantity}"

class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)
        print(f"Added {product.name} to the cart.")

    def remove_product(self, product_name):
        for product in self.items:
            if product.name == product_name:
                self.items.remove(product)
                print(f"Removed {product.name} from the cart.")
                return
        print("Product not found in the cart.")

    def view_cart(self):
        if not self.items:
            print("Your cart is empty.")
        else:
            print("Cart Items:")
            for product in self.items:
                print(product)

    def total_amount(self):
        total = sum(product.price * product.quantity for product in self.items)
        return total

# Example usage
p1 = Product("Laptop", 800, 1)
p2 = Product("Mouse", 20, 2)
p3 = Product("Keyboard", 50, 1)

cart = Cart()
cart.add_product(p1)
cart.add_product(p2)
cart.add_product(p3)

cart.view_cart()
print(f"Total Amount: ${cart.total_amount()}")

cart.remove_product("Mouse")
cart.view_cart()
print(f"Total Amount: ${cart.total_amount()}")

