import pandas as pd

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

def extract_files(file):
    df = pd.read_csv(file)
    df.info()
    # print(df)
    # return df

def cleaning_data(df, schema):
    df = df.astype(schema)
    # for column, dtype in schema.items():


def validate_data(customer_df, product_df, sale_df):
    pass
    valid_data = []
    invalid_data = []
    # No negative quantity
    # if sale_df['quantity'] < 0:
    #     print('Quantity has a negative value')
    # No null customer_id
    # if customer_df.isna() == True:
    #     print('Customer ID  has a null value')
    # Valid product_id exists in product table
    # if sale_df['product_id'].isin(product_df['product_id']) == True:
    #     pass
    # else:
    #     print('Product ID not present in the Product table')

def main():
    # read csv files
    customer_data = extract_files(customers_data)
    product_data = extract_files(products_data)
    sale_data = extract_files(sales_data)
    
    # clean csv files
    clean_customer_data = cleaning_data(customer_data, schemas["customers"])
    # clean_product_data = cleaning_data(product_data)
    # clean_sale_data = cleaning_data(sale_data)
    
    # validate data
    # validate_data(clean_customer_data, clean_product_data, clean_sale_data)

main()