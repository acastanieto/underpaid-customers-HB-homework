def customer_under_over_paid(file_name, melon_cost):

    """Calculates whether each customer over or underpaid for melons"""
    
    customer_orders = open(file_name)
    for order in customer_orders:
        order = order.rstrip()
        order_info = order.split("|")

        customer_name = order_info[1]
        customer_melons = int(order_info[2])
        customer_paid = float(order_info[3])

        customer_expected = customer_melons * melon_cost
        if customer_expected != customer_paid:
                print customer_name, "paid %.2f, expected %.2f" % (
                    customer_paid, customer_expected)  



customer_under_over_paid("customer-orders.txt", 1.00)