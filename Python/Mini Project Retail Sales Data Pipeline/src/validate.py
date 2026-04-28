import pandas as pd

def validate_data(customer_df, product_df, sale_df):
    bad_rows_list = []
    customer_df = customer_df.copy()
    product_df = product_df.copy()
    sale_df = sale_df.copy()
    
    # Null customer name
    condition = customer_df['name'].isna() == True
    bad_rows = customer_df[condition].copy()
    bad_rows['reason'] = "null customer name"
    bad_rows_list.append(bad_rows)
    customer_df = customer_df[~condition]

    # Null customer city
    condition = customer_df['city'].isna() == True
    bad_rows = customer_df[condition].copy()
    bad_rows['reason'] = "null customer city"
    bad_rows_list.append(bad_rows)
    customer_df = customer_df[~condition]

    # Null order_date
    condition = sale_df['order_date'].isna() == True
    bad_rows = sale_df[condition].copy()
    bad_rows['reason'] = "null order_date"
    bad_rows_list.append(bad_rows)
    sale_df = sale_df[~condition]

    # No negative quantity
    condition = sale_df['quantity'] < 0
    bad_rows = sale_df[condition].copy()
    bad_rows['reason'] = "negative quantity"
    bad_rows_list.append(bad_rows)
    sale_df = sale_df[~condition]

    # No null customer_id in customer_df
    condition = customer_df['customer_id'].isna() == True
    bad_rows = customer_df[condition].copy()
    bad_rows['reason'] = "null customer_id"
    bad_rows_list.append(bad_rows)
    customer_df = customer_df[~condition]

    # No null customer_id in sales_df
    condition = sale_df['customer_id'].isna() == True
    bad_rows = sale_df[condition].copy()
    bad_rows['reason'] = "null customer_id"
    bad_rows_list.append(bad_rows)
    sale_df = sale_df[~condition]

    # Valid product_id exists in product table
    condition = sale_df['product_id'].isin(product_df['product_id']) == False
    bad_rows = sale_df[condition].copy()
    bad_rows['reason'] = "product_id does not exist in product table"
    bad_rows_list.append(bad_rows)
    sale_df = sale_df[~condition]
    bad_df = pd.concat(bad_rows_list, ignore_index=True)

    return bad_df, customer_df, product_df, sale_df