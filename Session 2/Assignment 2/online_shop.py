class CartItem:
    def __init__(self, item_name, price, quantity=1):
        self.item_name = item_name
        self.price = price
        self.quantity = quantity

    def update_quantity(self, quantity):
        if quantity > 0:
            self.quantity = quantity
        else:
            print("Quantity must be at least 1.")

    def calculate_total(self):
        return self.price * self.quantity

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, price, quantity=1):
        if item_name in self.items:
            self.items[item_name].quantity += quantity
        else:
            self.items[item_name] = CartItem(item_name, price, quantity)
        print(f"Added {quantity} x {item_name} to the cart.")

    def remove_item(self, item_name, quantity=1):
        if item_name in self.items:
            if quantity > self.items[item_name].quantity:
                print("Error: Cannot remove more items than available in cart!")
            elif self.items[item_name].quantity > quantity:
                self.items[item_name].quantity -= quantity
                print(f"Removed {quantity} x {item_name} from the cart.")
            else:
                del self.items[item_name]
                print(f"Removed {item_name} from the cart.")
        else:
            print("Item not found in the cart!")

    def calculate_total(self):
        return sum(item.calculate_total() for item in self.items.values())

    def calculate(self):
        total = self.calculate_total()
        print(f"Total amount payable: ${total}")
        return total

    def show_cart(self):
        if not self.items:
            print("Your cart is empty.")
        else:
            print("\n===== Shopping Cart =====")
            for item in self.items.values():
                print(f"{item.item_name}: ${item.price} x {item.quantity} = ${item.calculate_total()}")
            print(f"Total: ${self.calculate_total()}")

# Main Program with Menu
def main():
    cart = ShoppingCart()

    while True:
        print("\n===== ONLINE SHOPPING CART MENU =====")
        print("1. View Cart")
        print("2. Add Item")
        print("3. Remove Item")
        print("4. Calculate Total")
        print("5. Checkout")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            cart.show_cart()
        elif choice == "2":
            item_name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            quantity = int(input("Enter quantity: "))
            cart.add_item(item_name, price, quantity)
        elif choice == "3":
            item_name = input("Enter item name to remove: ")
            quantity = int(input("Enter quantity to remove: "))
            cart.remove_item(item_name, quantity)
        elif choice == "4":
            cart.calculate()
        elif choice == "5":
            cart.show_cart()
            print("Proceeding to checkout...")
            break
        elif choice == "6":
            print("Thank you for shopping with us!")
            break
        else:
            print("Invalid option! Please try again.")

if __name__ == "__main__":
    main()
