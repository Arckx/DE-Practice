import pandas as pd
import logging

logging.basicConfig(filename='etl_project/app.txt', filemode='w', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(name)s - %(message)s')

files = ["etl_project/sales_jan.csv", "etl_project/sales_feb.csv", "etl_project/sales_mar.csv"]

def read_file(file):
    df = pd.read_csv(file)
    return df

def clean_data(df):
    df['product'] = df['product'].str.lower()
    df['category'] = df['category'].str.lower()
    df['price'] = df['price'].replace('ten', 10)
    logging.info(f'Count of dropped rows {df.isna().any(axis=1).sum()}')
    df =  df.dropna(subset=['quantity'])
    df['quantity'] = df['quantity'].astype(int)
    df['price'] = df['price'].astype(int)
    df.drop_duplicates(inplace=True)
    return df

def transform_data(df):
    df['total'] = df['price'] * df['quantity']
    return df

def aggregate_data(all_data):
    result = pd.concat(all_data, ignore_index=True)
    total_sales = result.groupby('category')['total'].sum().reset_index()
    return result, total_sales

def main():
    all_data = []
    for file in files:
        try:
            logging.info(f'Reading .csv file: {file}')
            dataframe = read_file(file)
            logging.info(f'Cleaning .csv file: {file}')
            cleaned_df = clean_data(dataframe)
            logging.info(f'Transforming .csv files: {file}')
            transformed_df = transform_data(cleaned_df)
            logging.info('Appending .csv files into an empty list')
            all_data.append(transformed_df)

        except Exception as e:
            logging.error(f'This is the error message: {file} {e}')

    # aggregate and save output
    logging.info('Concatenating the Dataframes into one table and Aggregating Total Sales based on category')
    if all_data:
        dataset, total_sales = aggregate_data(all_data)
        logging.info('Saving Concatenated dataframe and Aggregated dataframe separately to .csv')
        dataset.to_csv('etl_project/combined_data.csv', index=False)
        total_sales.to_csv('etl_project/total_sales.csv', index=False)
    else:
        logging.info('No valid data processed')

main()
