import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")

CUSTOMER_FILE = os.path.join(DATA_DIR, "customers.json")
PRODUCT_FILE = os.path.join(DATA_DIR, "products.json")
INVOICE_FILE = os.path.join(DATA_DIR, "invoices.json")

GST_RATE = 18
