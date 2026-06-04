class CartItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
class ShoppingCart:
    def __init__(self):
        self.items = []
    def add_item(self, item):
        self.items.append(item)
    def remove_item(self, name):
        self.items = [
            item for item in self.items
            if item.name != name
        ]
    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.price * item.quantity
        return total
    
    def print_receipt(self):
        print("Shopping Cart Receipt")
        for item in self.items:
            print(f"{item.name} - {item.quantity} x {item.price}")
        subtotal = self.calculate_total()
        gst = subtotal * 0.18
        final_total = subtotal + gst

        print("\nSubtotal:", subtotal)
        print("GST (18%):", gst)
        print("Final Total:", final_total)

cart = ShoppingCart()
cart.add_item(CartItem("Laptop", 50000, 1))
cart.add_item(CartItem("Mouse", 500, 2))
cart.print_receipt()