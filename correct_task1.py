# Write your corrected implementation for Task 1 here.
# Do not modify `task1.py`.
def calculate_average_order_value(orders):
    if not orders:
        return 0

    total = 0
    count = 0
    
    for order in orders:
        if (
            isinstance(order, dict)
            and order.get("status") != "cancelled"
            and isinstance(order.get("amount"), (int, float))
            and order["amount"] >= 0
        ):
            total += order["amount"]
            count += 1
            print(total)
            print(count)    
    return total / count if count else 0

