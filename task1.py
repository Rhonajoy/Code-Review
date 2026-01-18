def calculate_average_order_value(orders):
    total = 0
    count = len(orders)
    print(count)
    print (total)

    for order in orders:
        if order["status"] != "cancelled":
            total += order["amount"]
            print(total)

    print( total / count)
calculate_average_order_value([ {"status": "completed", "amount": 100},
    {"status": "cancelled", "amount": 50}])