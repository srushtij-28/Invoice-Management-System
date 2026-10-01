from config import CUSTOMER_FILE
from storage import load_data, save_data
from utils import generate_id, find_by_id


def add_customer():
    customers = load_data(CUSTOMER_FILE)

    name = input("Enter customer name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()

    if not name:
        print("Customer name cannot be empty.")
        return

    customer = {
        "id": generate_id(customers, "C"),
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    customers.append(customer)

    save_data(CUSTOMER_FILE, customers)

    print(f"Customer added successfully.")
    print(f"Customer ID: {customer['id']}")


def view_customers():
    customers = load_data(CUSTOMER_FILE)

    if not customers:
        print("No customers found.")
        return

    print("\n" + "=" * 70)
    print("CUSTOMERS")
    print("=" * 70)

    for customer in customers:
        print(f"ID      : {customer['id']}")
        print(f"Name    : {customer['name']}")
        print(f"Phone   : {customer['phone']}")
        print(f"Email   : {customer['email']}")
        print(f"Address : {customer['address']}")
        print("-" * 70)


def search_customer():
    customers = load_data(CUSTOMER_FILE)

    keyword = input("Enter customer name or ID: ").strip().lower()

    results = [
        customer
        for customer in customers
        if keyword in customer["name"].lower()
        or keyword in customer["id"].lower()
    ]

    if not results:
        print("No customer found.")
        return

    for customer in results:
        print(
            f"{customer['id']} | "
            f"{customer['name']} | "
            f"{customer['phone']} | "
            f"{customer['email']}"
        )


def delete_customer():
    customers = load_data(CUSTOMER_FILE)

    customer_id = input("Enter customer ID: ").strip()

    customer = find_by_id(customers, customer_id)

    if not customer:
        print("Customer not found.")
        return

    customers.remove(customer)

    save_data(CUSTOMER_FILE, customers)

    print("Customer deleted successfully.")
