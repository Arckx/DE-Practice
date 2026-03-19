customers = [
    {"customer_id": 101, "name": "Ahmed Khan", "city": "Karachi"},
    {"customer_id": 102, "name": "Sara Ali", "city": "Lahore"},
    {"customer_id": 103, "name": "John Mathews", "city": "karachi"},
    {"customer_id": 104, "name": "Fatima Noor", "city": None},
    {"customer_id": 105, "name": "Usman Tariq", "city": "Islamabad"}
]

products = [
    {"product_id": "P001", "product_name": "Laptop Bag", "category": "Accessories", "price": 2500},
    {"product_id": "P002", "product_name": "Wireless Mouse", "category": "Electronics", "price": 1200},
    {"product_id": "P003", "product_name": "Keyboard", "category": "electronics", "price": 1800},
    {"product_id": "P004", "product_name": "Notebook", "category": "Stationery", "price": 300}
]

orders = [
    {"order_id": 5001, "customer_id": 101, "product_id": "P001", "quantity": 2, "order_date": "2024-01-15"},
    {"order_id": 5002, "customer_id": 102, "product_id": "P002", "quantity": 1, "order_date": "2024-01-18"},
    {"order_id": 5003, "customer_id": 103, "product_id": "P003", "quantity": 1, "order_date": "2024-01-20"},
    {"order_id": 5004, "customer_id": 104, "product_id": "P010", "quantity": 3, "order_date": "2024-01-25"},
    {"order_id": 5005, "customer_id": 101, "product_id": "P002", "quantity": 2, "order_date": "2024-02-03"},
    {"order_id": 5006, "customer_id": 105, "product_id": "P004", "quantity": 5, "order_date": "2024-02-10"}
]

payments = [
    {"payment_id": "PAY001", "order_id": 5001, "amount_paid": 5000},
    {"payment_id": "PAY002", "order_id": 5002, "amount_paid": 1200},
    {"payment_id": "PAY003", "order_id": 5003, "amount_paid": 1500},
    {"payment_id": "PAY004", "order_id": 5005, "amount_paid": 2400},
    {"payment_id": "PAY005", "order_id": 5010, "amount_paid": 999}
]

# Part 1: Validate the data
## customers with missing city
for customer in customers:
    if customer:
        for key, value in customer.items():
            if customer["city"] == None:
                print(customer[key])

## inconsistent city naming
for customer in customers:
    if customer:
        for key, value in customer.items():
            if customer["city"]:
                customer["city"] = customer["city"].lower()
        print(customer)

## inconsistent category naming
for product in products:
    if product:
        for key, value in product.items():
            if product["category"]:
                product["category"] = product["category"].lower()
        print(product)

## orders with invalid product_id
product_list = set()
for product in products:
    if product:
        for key, value in product.items():
            if product["product_id"]:
                # print(product["product_id"])
                product_list.add(product["product_id"])

for order in orders:
    if order:
        for key, value in order.items():
            if order["product_id"] not in product_list:
                print(order[key])

## payments with invalid order_id
order_list = set()
for order in orders:
    if order:
        for key, value in order.items():
            if order["order_id"]:
                order_list.add(order["order_id"])

for payment in payments:
    if payment:
        for key, value in payment.items():
            if payment["order_id"] not in order_list:
                print(payment[key])

print(order_list)

## Part 2: Clean the data
## standardize city names
cleaned_customers = []
for customer in customers:
    if customer:
        for key, value in customer.items():
            if customer["city"]:
                customer["city"] = customer["city"].lower()
        cleaned_customers.append(customer)
print(cleaned_customers)

## standardize category names
cleaned_products = []
for product in products:
    if product:
        for key, value in product.items():
            if product["category"]:
                product["category"] = product["category"].lower()
        cleaned_products.append(product)
print(cleaned_products)

## separate valid orders from invalid orders
valid_orders = []
invalid_orders = []
for order in orders:
    if order:
        for key, value in order.items():
            if order["product_id"] not in product_list:
                invalid_orders.append(order[key])
            else:
                valid_orders.append(order[key])

## keep invalid records in a separate rejected list
print("valid: ", valid_orders)
print("invalid: ", invalid_orders)


## Part 3: Transform the data
## Create lookup structures so you can work efficiently:
## customers by customer_id
customer_lookup = {}
for customer in customers:
    customer_id = customer["customer_id"]
    customer_lookup[customer_id] = customer
# print("customer_lookup: \n", customer_lookup)
## products by product_id
product_lookup = {}
for product in products:
    product_id = product["product_id"]
    product_lookup[product_id] = product
# print("product_lookup: \n", product_lookup)
## payments by order_id
payment_lookup = {}
for payment in payments:
    order_id = payment["order_id"]
    payment_lookup[order_id] = payment
# print("payment_lookup: \n", payment_lookup)
## Then create an order summary dataset where each 
## valid order contains combined information like:
## order_id
## customer_name
## city
## product_name
## category
## quantity
## price
## expected_amount
## amount_paid
## payment_status

order_summary = []
for order in orders:
    payment_status = "Unpaid"
    customer_id = order["customer_id"]
    product_id = order["product_id"]
    order_id = order["order_id"]
    quantity = order["quantity"]
    if customer_id in customer_lookup:
        customer_name = customer_lookup[customer_id]['name']
        customer_city = customer_lookup[customer_id]['city']
        if product_id in product_lookup:
            product_name = product_lookup[product_id]['product_name']
            category = product_lookup[product_id]['category']
            price = product_lookup[product_id]['price']
            expected_amount = quantity * price
            if order_id in payment_lookup:
                amount_paid = payment_lookup[order_id]['amount_paid']
                if expected_amount == amount_paid:
                    payment_status = "Paid"
                else:
                    payment_status = "Partially Paid"
    summary_row = {
        "order_id": order_id,
        "customer_name": customer_name,
        "city": customer_city,
        "product_name": product_name,
        "category": category,
        "quantity": quantity,
        "price": price,
        "expected_amount": expected_amount,
        "amount_paid": amount_paid,
        "payment_status": payment_status
        }
    order_summary.append(summary_row)


