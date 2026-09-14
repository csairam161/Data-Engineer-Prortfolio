import re
from datetime import datetime
def validate_customer(customer):
    """
    Validate a customer record from customers.json.
    Returns a list of data-quality errors.
    """
    errors = []
    required_fields = [
        "customer_id",
        "first_name",
        "last_name",
        "email",
        "state",
        "created_date"
    ]
    # Check required fields
    for field in required_fields:
        if not customer.get(field):
            errors.append(f"Missing required field: {field}")
    # Validate customer ID
    customer_id = customer.get("customer_id", "")
    if customer_id and not re.fullmatch(r"C\d{4}", customer_id):
        errors.append("Invalid customer_id format")
    # Validate email
    email = customer.get("email", "")
    if email and not re.fullmatch(
        r"[^@\s]+@[^@\s]+\.[^@\s]+",
        email
    ):
        errors.append("Invalid email address")
    # Validate state
    state = customer.get("state", "")
    if state and not re.fullmatch(r"[A-Z]{2}", state):
        errors.append("State must be a 2-letter uppercase code")
    # Validate date
    created_date = customer.get("created_date", "")
    if created_date:
        try:
            datetime.strptime(created_date, "%Y-%m-%d")
        except ValueError:
            errors.append("Invalid created_date; expected YYYY-MM-DD")
    return errors
def validate_order(order, valid_customer_ids):
    """
    Validate an order record extracted from orders.xml.
    """
    errors = []
    required_fields = [
        "order_id",
        "customer_id",
        "order_date",
        "amount",
        "status"
    ]
    # Check required fields
    for field in required_fields:
        if not order.get(field):
            errors.append(f"Missing required field: {field}")
    # Referential integrity
    customer_id = order.get("customer_id")
    if customer_id and customer_id not in valid_customer_ids:
        errors.append(
            f"Customer {customer_id} does not exist in customer source"
        )
    # Validate amount
    amount = order.get("amount")
    if amount:
        try:
            if float(amount) < 0:
                errors.append("Order amount cannot be negative")
        except ValueError:
            errors.append("Order amount must be numeric")
    # Validate date
    order_date = order.get("order_date", "")
    if order_date:
        try:
            datetime.strptime(order_date, "%Y-%m-%d")
        except ValueError:
            errors.append("Invalid order_date; expected YYYY-MM-DD")
    return errors
