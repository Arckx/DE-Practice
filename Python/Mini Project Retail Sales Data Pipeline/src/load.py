import pandas as pd

def load_data(good_data, bad_data):
    good_data.to_csv("output/clean_sales.csv", index=False)
    bad_data.to_csv("output/bad_data.csv", index=False)