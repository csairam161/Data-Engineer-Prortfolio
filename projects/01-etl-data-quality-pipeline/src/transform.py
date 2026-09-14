from datetime import datetime
def transform_customer(customer):
    """Clean and standardize customer data."""
    return {
        "customer_id": customer["customer_id"].strip().upper(),
        "first_name": customer["first_name"].strip().title(),
        "last_name": customer["last_name"].strip().title(),
        "email": customer["email"].strip().lower(),
        "state": customer["state"].strip().upper(),
        "created_date": customer["created_date"]
    }
def transform_order(order):
    """Clean and standardize order data."""
    return {
        "order_id": order["order_id"].strip().upper(),
        "customer_id": order["customer_id"].strip().upper(),
        "order_date": order["order_date"],
        "amount": round(float(order["amount"]), 2),
        "status": order["status"].strip().upper()
    }
def add_processing_metadata(record):
    """Add ETL processing timestamp."""
    transformed_record = record.copy()
    transformed_record["processed_at"] = (
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    return transformed_record

