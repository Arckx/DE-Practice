import pandas as pd

def cleaning_data(df, schema):
    for column, dtype in schema.items():
        if dtype == "datetime":
            df[column] = pd.to_datetime(df[column], errors='coerce')
        else:
            df[column] = df[column].astype(dtype)

    return df

def transform_data(customer_df, product_df, sale_df):
    joined_data = pd.merge(customer_df, sale_df, on='customer_id', how='inner')
    result = pd.merge(joined_data, product_df, on='product_id', how='inner')
    result['total_amount'] = result['quantity'] * result['price']
    result['order_month'] = result['order_date'].dt.month

    return result

def aggregate_data(df):
    total_sales_per_city  = df.groupby('city')['total_amount'].sum()
    top_selling_product = df.groupby('product_name')['quantity'].sum()
    monthly_revenue = df.groupby('order_month')['total_amount'].sum()

    return total_sales_per_city, top_selling_product, monthly_revenue

    