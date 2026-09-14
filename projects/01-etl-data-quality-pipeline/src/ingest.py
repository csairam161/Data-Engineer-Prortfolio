import json
import xml.etree.ElementTree as ET
from pathlib import Path
# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
def load_customers_json():
    """Read customer records from the JSON source file."""
    file_path = DATA_DIR / "customers.json"
    with open(file_path, "r", encoding="utf-8") as file:
        customers = json.load(file)
    print(f"Customers loaded: {len(customers)}")
    return customers
def load_orders_xml():
    """Read order records from the XML source file."""
    file_path = DATA_DIR / "orders.xml"
    tree = ET.parse(file_path)
    root = tree.getroot()
    orders = []
    for order in root.findall(".//order"):
        record = {}
        for element in order:
            record[element.tag] = element.text
        orders.append(record)
    print(f"Orders loaded: {len(orders)}")
    return orders
def main():
    print("Starting source data ingestion...")
    customers = load_customers_json()
    orders = load_orders_xml()
    print("\nIngestion completed successfully.")
    print(f"Total customer records: {len(customers)}")
    print(f"Total order records: {len(orders)}")
if __name__ == "__main__":
    main()
