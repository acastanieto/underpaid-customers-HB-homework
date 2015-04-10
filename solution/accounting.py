MELON_COST = 1.00


def melon_payment_calculator(payment_data):
    """Calculate cost of melons and determine who has underpaid."""

    payment_data = open(payment_data)

    for line in payment_data:
        order = line.split('|')

        customer_name = order[1]
        customer_first = customer_name.split(" ")[0]
        customer_melons = float(order[2])
        customer_paid = float(order[3])

        customer_expected = customer_melons * MELON_COST

        if customer_expected < customer_paid:
            print customer_name, "paid %.2f, expected %.2f" % (
                customer_paid, customer_expected)
            print customer_first, "has overpaid for their melons."

        elif customer_expected > customer_paid:
            print customer_name, "paid %.2f, expected %.2f" % (
                customer_paid, customer_expected)
            print customer_first, "has underpaid for their melons."


melon_payment_calculator("customer-orders.txt")