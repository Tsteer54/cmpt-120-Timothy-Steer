from product import Product

products = [
    Product("Ultrasonic Range Finder", 2.50, 4),
    Product("Servo Motor", 14.99, 10),
    Product("Servo Controller", 44.95, 5),
    Product("Microcontroller Board", 34.95, 7),
    Product("Laser range finder", 149.99, 2),
    Product("Lithium polymer battery", 8.99, 8)
]


def print_stock():
    for i in range(len(products)):
        if products[i].quantity > 0:
            print(
                f"{i}) {products[i].name} {products[i].price} ({products[i].quantity} left)")


def main():
    print("This program lets you buy stuff.")
    cash = float(input("Please enter how much money you have: "))

    while cash > 0.0:
        print_stock()
        user_input = input(
            "Please enter product ID and quantity separated by space: ").split(" ")
        if user_input[0].lower() == "quit":
            break

        prod_id = int(user_input[0])
        quantity = int(user_input[1])

        if products[prod_id].in_stock(quantity):
            if cash > products[prod_id].price * quantity:
                cash -= products[prod_id].price * quantity
                products[prod_id].quantity -= quantity
                print(
                    f"You purchased {quantity} of {products[prod_id].name}. You have ${cash} left.")
            else:
                print("Sorry you can afford that.")
        else:
            print("Sorry we are all out!")


main()
