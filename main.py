import os

from config import DATA_DIR, CUSTOMER_FILE, PRODUCT_FILE, INVOICE_FILE
from storage import save_data

from customer_manager import (
    add_customer,
    view_customers,
    search_customer,
    delete_customer
)

from product_manager import (
    add_product,
    view_products,
    search_product,
    delete_product
)

from invoice_manager import (
    create_invoice,
    view_invoices,
    search_invoice,
    delete_invoice
)


def initialize_files():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    files = [
        CUSTOMER_FILE,
        PRODUCT_FILE,
        INVOICE_FILE
    ]

    for file in files:
        if not os.path.exists(file):
            save_data(file, [])


def show_menu():
    print("\n")
    print("=" * 55)
    print("          INVOICE MANAGEMENT SYSTEM")
    print("=" * 55)

    print("\nCUSTOMERS")
    print("1. Add Customer")
    print("2. View Customers")
    print("3. Search Customer")
    print("4. Delete Customer")

    print("\nPRODUCTS")
    print("5. Add Product")
    print("6. View Products")
    print("7. Search Product")
    print("8. Delete Product")

    print("\nINVOICES")
    print("9. Create Invoice")
    print("10. View Invoices")
    print("11. Search Invoice")
    print("12. Delete Invoice")

    print("\n13. Exit")

    print("=" * 55)


def main():
    initialize_files()

    while True:
        show_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_customer()

        elif choice == "2":
            view_customers()

        elif choice == "3":
            search_customer()

        elif choice == "4":
            delete_customer()

        elif choice == "5":
            add_product()

        elif choice == "6":
            view_products()

        elif choice == "7":
            search_product()

        elif choice == "8":
            delete_product()

        elif choice == "9":
            create_invoice()

        elif choice == "10":
            view_invoices()

        elif choice == "11":
            search_invoice()

        elif choice == "12":
            delete_invoice()

        elif choice == "13":
            print("Thank you for using Invoice Management System.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
