import logging
import pandas as pd

logging.basicConfig(filename = 'python_activity.txt', level = logging.INFO, filemode='w', format = "%(asctime)s - %(levelname)s - %(lineno)d - %(message)s")

logging.info("Program has Started")

# DataSet Definition
logging.info("DataSet Definition")
products = [
{"product_id": 1, "product_name": "Notebook", "price": 5, "cost": 2},
{"product_id": 2, "product_name": "Pen", "price": 1, "cost": 0.3},
{"product_id": 3, "product_name": "Pencil", "price": 1, "cost": 0.2},
{"product_id": 4, "product_name": "Eraser", "price": 0.5, "cost": 0.2},
{"product_id": 5, "product_name": "Marker", "price": 2, "cost": 0.5},
{"product_id": 6, "product_name": "Stapler", "price": 4, "cost": 1},
{"product_id": 7, "product_name": "Tape", "price": 2, "cost": 0.7},
{"product_id": 8, "product_name": "Glue", "price": 3, "cost": 1},
{"product_id": 9, "product_name": "Highlighter", "price": 2, "cost": 0.6},
{"product_id": 10, "product_name": "Scissors", "price": 6, "cost": 2},
{"product_id": 11, "product_name": "Folder", "price": 3, "cost": 1},
{"product_id": 12, "product_name": "Ruler", "price": 2, "cost": 1.5},
{"product_id": 13, "product_name": "Calculator", "price": 15, "cost": 9},
{"product_id": 14, "product_name": "Sharpener", "price": 1, "cost": 0.4},
{"product_id": 15, "product_name": "Binder", "price": 5, "cost": 3},
{"product_id": 16, "product_name": "Clipboard", "price": 7, "cost": 4},
{"product_id": 17, "product_name": "Sticky Notes", "price": 3, "cost": 1.5},
{"product_id": 18, "product_name": "Whiteboard Marker", "price": 4, "cost": 2},
{"product_id": 19, "product_name": "Paper Pack", "price": 10, "cost": 7},
{"product_id": 20, "product_name": "Desk Organizer", "price": 12, "cost": 10}
]

transactions = [
{"transaction_id": 1, "product_id": 2, "quantity": 10},
{"transaction_id": 2, "product_id": 1, "quantity": 5},
{"transaction_id": 3, "product_id": 5, "quantity": 3},
{"transaction_id": 4, "product_id": 3, "quantity": 12},
{"transaction_id": 5, "product_id": 10, "quantity": 2},
{"transaction_id": 6, "product_id": 7, "quantity": 6},
{"transaction_id": 7, "product_id": 4, "quantity": 15},
{"transaction_id": 8, "product_id": 6, "quantity": 4},
{"transaction_id": 9, "product_id": 9, "quantity": 8},
{"transaction_id": 10, "product_id": 12, "quantity": 7},
{"transaction_id": 11, "product_id": 14, "quantity": 9},
{"transaction_id": 12, "product_id": 8, "quantity": 3},
{"transaction_id": 13, "product_id": 13, "quantity": 1},
{"transaction_id": 14, "product_id": 11, "quantity": 5},
{"transaction_id": 15, "product_id": 15, "quantity": 4},
{"transaction_id": 16, "product_id": 16, "quantity": 2},
{"transaction_id": 17, "product_id": 18, "quantity": 6},
{"transaction_id": 18, "product_id": 19, "quantity": 3},
{"transaction_id": 19, "product_id": 20, "quantity": 2},
{"transaction_id": 20, "product_id": 17, "quantity": 5}
]



#Data Validation
def transaction_validation(transaction):
    logging.info("Validating transaction data")
    product = product_lookup(transaction["product_id"])
    if product is None or transaction["quantity"] <= 0:
        return False
    return True
logging.info("Transaction Data successfully validated")

#Data Processing
def product_lookup(product_id):
    logging.info("Validating If Product ID exists")
    for product in products:
        if product["product_id"] == product_id:
            return product
        logging.info("Product ID exists")
    return None

def revenue_calculation(transaction):
    logging.info("Calculating Revenue per product")
    if not transaction_validation(transaction):
        return 0
    product = product_lookup(transaction["product_id"])
    logging.info("Revenue Calculated")
    return product["price"] * transaction["quantity"]


# print(revenue_calculation(transactions[1]))

def highest_revenue(transaction, products):
    logging.info("Finding the product that genetates the highest revenue")
    high = 0
    best_product = None
    for record in transaction:
        for product in products:
            if record['product_id'] == product['product_id']:
                revenue = record['quantity'] * product['price']
                if high < revenue:
                    high = revenue
                    best_product = product['product_name']
                logging.info("Found the product with highest revenue")

    print("Revenue Generated:", high)
    print("Best Product:", best_product)

# highest_revenue(transactions, products)    

logging.info("Converting list of dictionaries into separate dataframes")
product_list = pd.DataFrame(products)
# product_list.to_csv("python_activity_products.csv", index=False)

transaction_list = pd.DataFrame(transactions)
# transaction_list.to_csv("python_activity_transactions.csv", index=False)

# print(product_list)

logging.info("Merging two dataframes into one as inner join")
order_details = pd.merge(product_list, transaction_list, left_on= 'product_id', right_on= 'product_id', how= 'inner')

logging.info("Creation of a new column revenue")
order_details['revenue'] = order_details['price'] * order_details['quantity']

logging.info("Creation of a new column profit")
order_details['profit'] = order_details['revenue'] - (order_details['quantity'] * order_details['cost'])
groupby_product_name = order_details.groupby('product_name').sum().sort_values(by='quantity', ascending=False)
print(groupby_product_name)
