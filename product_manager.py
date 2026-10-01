from config import PRODUCT_FILE
from storage import load_data, save_data
from utils import generate_id, find_by_id


def add_product():
    products = load_data(PRODUCT_FILE)

    name = input("Enter product name: ").strip()

    try:
        price = float(input("Enter product price: "))
    except ValueError:
        print("Invalid price.")
        return

    if price < 0:
        print("Price cannot be negative.")
        return

    product = {
        "id": generate_id(products, "P"),
        "name": name,
        "price": price
    }

    products.append(product)

    save_data(PRODUCT_FILE, products)

    print("Product added successfully.")
    print(f"Product ID: {product['id']}")


def view_products():
    products = load_data(PRODUCT_FILE)

    if not products:
        print("No products found.")
        return

    print("\n" + "=" * 60)
    print("PRODUCTS")
    print("=" * 60)

    for product in products:
        print(
            f"ID: {product['id']} | "
            f"Name: {product['name']} | "
            f"Price: ₹{product['price']:.2f}"
        )


def search_product():
    products = load_data(PRODUCT_FILE)

    keyword = input("Enter product name or ID: ").strip().lower()

    results = [
        product
        for product in products
        if keyword in product["name"].lower()
        or keyword in product["id"].lower()
    ]

    if not results:
        print("No product found.")
        return

    for product in results:
        print(
            f"{product['id']} | "
            f"{product['name']} | "
            f"₹{product['price']:.2f}"
        )


def delete_product():
    products = load_data(PRODUCT_FILE)

    product_id = input("Enter product ID: ").strip()

    product = find_by_id(products, product_id)

    if not product:
        print("Product not found.")
        return

    products.remove(product)

    save_data(PRODUCT_FILE, products)

    print("Product deleted successfully.")
