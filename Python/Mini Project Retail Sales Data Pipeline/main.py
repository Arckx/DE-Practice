import pandas as pd

customers_data = 'data/customers.csv'
products_data = 'data/products.csv'
sales_data = 'data/sales.csv'

def extract_files(file):
    df = pd.read_csv(file)
    return df

def cleaning_data(df):
    if 'quantity' in df.columns:
        df['quantity'] = df['quantity'].abs()
    return df

def validate_data(customer_df, product_df, sale_df):
    valid_data = []
    invalid_data = []
    # No negative quantity
    if sale_df['quantity'] < 0:
        print('Quantity has a negative value')
    # No null customer_id
    if customer_df.isna() == True:
        print('Customer ID  has a null value')
    # Valid product_id exists in product table
    if sale_df['product_id'].isin(product_df['product_id']) == True:
        pass
    else:
        print('Product ID not present in the Product table')

def main():
    # read csv files
    customer_data = extract_files(customers_data)
    product_data = extract_files(products_data)
    sale_data = extract_files(sales_data)
    # clean csv files
    clean_customer_data = cleaning_data(customer_data)
    clean_product_data = cleaning_data(product_data)
    clean_sale_data = cleaning_data(sale_data)
    print(clean_sale_data)
    # validate data
    validate_data(clean_customer_data, clean_product_data, clean_sale_data)

main()