
def show_cart(cart):

    if not cart:
        print("Cart is empty")
        return

    print("Shopping Cart Items:", cart)

cart = [100, 250, 75]

show_cart(cart)