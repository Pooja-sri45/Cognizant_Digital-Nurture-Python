class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock
class Perishable(Product):
    def category(self):
        return "Perishable"
class Electronics(Product):
    def category(self):
        return "Electronics"
inventory = {}
low_stock = set()

p1 = Perishable("Milk", 5)
p2 = Electronics("Laptop", 20)
p3 = Perishable("Bread", 2)

inventory[p1.name] = p1.stock
inventory[p2.name] = p2.stock
inventory[p3.name] = p3.stock
for product, stock in inventory.items():
    if stock < 5:
        low_stock.add(product)
print("Inventory Summary\n")
for product, stock in inventory.items():
    print(f"Product: {product}")
    print(f"Stock: {stock}")
    print()
print("Low Stock Alerts")
for item in low_stock:
    print(item)