import pandas as pd
import logging

from src.extract import extract_files
from src.transform import cleaning_data, transform_data, aggregate_data
from src.validate import validate_data
from src.load import load_data

logging.basicConfig(filename='logs/log.txt', filemode='w', level=logging.INFO)

customers_data = 'data/customers.csv'
products_data = 'data/products.csv'
sales_data = 'data/sales.csv'

schemas = {
    "sales":     { "order_id": "int",
                    "customer_id": "str",
                    "product_id": "str",
                    "order_date": "datetime",
                    "quantity": "int",
                    "price": "float" },
    "customers": { "customer_id": "str", 
                    "name": "str",
                    "city": "str" },
    "products":  { "product_id": "str",
                    "product_name": "str",
                    "category": "str" }
}
    

def main():
    # read csv files
    customer_data = extract_files(customers_data)
    product_data = extract_files(products_data)
    sale_data = extract_files(sales_data)
    
    # clean csv files
    clean_customer_data = cleaning_data(customer_data, schemas["customers"])
    clean_product_data = cleaning_data(product_data, schemas["products"])
    clean_sale_data = cleaning_data(sale_data, schemas["sales"])

    # validate data
    bad_data, vcustomer_data, vproduct_data, vsale_data = validate_data(clean_customer_data, clean_product_data, clean_sale_data)
    # print(bad_data, vcustomer_data, vproduct_data, vsale_data)

    # transform data
    transformed_data = transform_data(vcustomer_data, vproduct_data, vsale_data)

    # aggregate data
    total_sales_per_city, top_selling_product, monthly_revenue = aggregate_data(transformed_data)

    logging.info(f"Total rows processed: {sale_data.shape[0]}")
    logging.info(f"Invalid rows: {bad_data.shape[0]}")
    logging.info(f"Clean rows: {transformed_data.shape[0]}")

    # load data
    load_data(transformed_data, bad_data)

main()