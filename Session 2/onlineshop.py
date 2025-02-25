class CartItem:
    def __init__(self, item_name, price, quantity):
        self.item_name = item_name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        return self.price * self.quantity

class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_item(self, item):
        self.cart.append(item)
        print(f"{item.item_name} (x{item.quantity}) added to the cart.")

    def remove_item(self, item_name):
        for item in self.cart:
            if item.item_name == item_name:
                self.cart.remove(item)
                print(f"{item_name} removed from the cart.")
                return
        print(f"{item_name} not found in the cart.")

    def show_cart(self):
        print("\nShopping Cart:")
        total_price = 0
        for item in self.cart:
            total_price += item.calculate_total()
            print(f"- {item.item_name} (x{item.quantity}) - ${item.calculate_total()}")
        print(f"Total Price: ${total_price}")

# Contoh penggunaan
cart = ShoppingCart()
item1 = CartItem("Laptop", 1200, 1)
item2 = CartItem("Headphones", 100, 2)

cart.add_item(item1)
cart.add_item(item2)

cart.show_cart()

cart.remove_item("Headphones")
cart.show_cart()
