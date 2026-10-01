from config import (
    CUSTOMER_FILE,
    PRODUCT_FILE,
    INVOICE_FILE,
    GST_RATE
)

from storage import load_data, save_data
from utils import generate_id, find_by_id, get_date


def create_invoice():
    customers = load_data(CUSTOMER_FILE)
    products = load_data(PRODUCT_FILE)
    invoices = load_data(INVOICE_FILE)

    if not customers:
        print("Please add a customer first.")
        return

    if not products:
        print("Please add a product first.")
        return

    customer_id = input("Enter customer ID: ").strip()

    customer = find_by_id(customers, customer_id)

    if not customer:
        print("Customer not found.")
        return

    invoice_items = []

    while True:
        print("\nAvailable Products:")
        for product in products:
            print(
                f"{product['id']} - "
                f"{product['name']} - "
                f"₹{product['price']:.2f}"
            )

        product_id = input(
            "\nEnter product ID or type DONE: "
        ).strip()

        if product_id.lower() == "done":
            break

        product = find_by_id(products, product_id)

        if not product:
            print("Product not found.")
            continue

        try:
            quantity = int(input("Enter quantity: "))
        except ValueError:
            print("Invalid quantity.")
            continue

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

        amount = product["price"] * quantity

        invoice_items.append({
            "product_id": product["id"],
            "product_name": product["name"],
            "price": product["price"],
            "quantity": quantity,
            "amount": amount
        })

        print("Product added to invoice.")

    if not invoice_items:
        print("Invoice must contain at least one product.")
        return

    subtotal = sum(item["amount"] for item in invoice_items)

    gst_amount = subtotal * GST_RATE / 100

    grand_total = subtotal + gst_amount

    invoice = {
        "id": generate_id(invoices, "INV"),
        "date": get_date(),
        "customer_id": customer["id"],
        "customer_name": customer["name"],
        "items": invoice_items,
        "subtotal": round(subtotal, 2),
        "gst_rate": GST_RATE,
        "gst_amount": round(gst_amount, 2),
        "grand_total": round(grand_total, 2)
    }

    invoices.append(invoice)

    save_data(INVOICE_FILE, invoices)

    print("\nInvoice created successfully.")
    print(f"Invoice ID: {invoice['id']}")
    print(f"Subtotal: ₹{subtotal:.2f}")
    print(f"GST: ₹{gst_amount:.2f}")
    print(f"Grand Total: ₹{grand_total:.2f}")


def view_invoices():
    invoices = load_data(INVOICE_FILE)

    if not invoices:
        print("No invoices found.")
        return

    for invoice in invoices:
        print("\n" + "=" * 70)
        print(f"Invoice ID : {invoice['id']}")
        print(f"Date       : {invoice['date']}")
        print(f"Customer   : {invoice['customer_name']}")
        print("-" * 70)

        for item in invoice["items"]:
            print(
                f"{item['product_name']} | "
                f"Qty: {item['quantity']} | "
                f"₹{item['amount']:.2f}"
            )

        print("-" * 70)
        print(f"Subtotal   : ₹{invoice['subtotal']:.2f}")
        print(f"GST        : ₹{invoice['gst_amount']:.2f}")
        print(f"Grand Total: ₹{invoice['grand_total']:.2f}")


def search_invoice():
    invoices = load_data(INVOICE_FILE)

    keyword = input(
        "Enter invoice ID or customer name: "
    ).strip().lower()

    results = [
        invoice
        for invoice in invoices
        if keyword in invoice["id"].lower()
        or keyword in invoice["customer_name"].lower()
    ]

    if not results:
        print("No invoice found.")
        return

    for invoice in results:
        print(
            f"{invoice['id']} | "
            f"{invoice['customer_name']} | "
            f"{invoice['date']} | "
            f"₹{invoice['grand_total']:.2f}"
        )


def delete_invoice():
    invoices = load_data(INVOICE_FILE)

    invoice_id = input("Enter invoice ID: ").strip()

    invoice = find_by_id(invoices, invoice_id)

    if not invoice:
        print("Invoice not found.")
        return

    invoices.remove(invoice)

    save_data(INVOICE_FILE, invoices)

    print("Invoice deleted successfully.")
