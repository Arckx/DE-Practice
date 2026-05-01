# Retail Sales Data Pipeline

A mini ETL (Extract, Transform, Load) pipeline built with Python and Pandas to process messy retail data from multiple CSV sources into clean, analytics-ready datasets.

---

## Project Structure

```
project/
│── data/
│    ├── sales.csv
│    ├── customers.csv
│    └── products.csv
│── output/
│    ├── clean_sales.csv
│    └── bad_data.csv
│── logs/
│    └── log.txt
└── main.py
```

---

## Pipeline Stages

### 1. Extract
Loads all three CSV files into Pandas DataFrames using a reusable `extract_files()` function.

### 2. Clean
Applies a per-file schema to enforce correct data types — dates as datetime, numeric fields as int/float, and IDs as strings. Handles parsing errors gracefully without crashing the pipeline.

### 3. Validate
Runs business rule checks on the data and separates records into good and bad:

| Rule | File |
|---|---|
| Null customer name | customers.csv |
| Null customer city | customers.csv |
| Null order date | sales.csv |
| Negative quantity | sales.csv |
| Null customer ID | sales.csv |
| Invalid product ID (not in products table) | sales.csv |

Each rejected row is tagged with a `reason` column explaining why it failed.

### 4. Transform
Joins validated sales, customer, and product data into a single enriched DataFrame and adds:
- `total_amount` = quantity × price
- `order_month` = month extracted from order_date

### 5. Aggregate
Generates business insights from the cleaned data:
- **Total sales per city**
- **Top-selling product** (by quantity)
- **Monthly revenue**

### 6. Load
Saves final outputs:
- `output/clean_sales.csv` — validated and enriched records
- `output/bad_data.csv` — rejected records with rejection reasons

---

## Data Quality Logging

The pipeline logs key metrics to `logs/log.txt` on every run:

```
Total rows processed: 6
Invalid rows: 2
Clean rows: 4
```

---

## Concepts Practiced

- ETL pipeline thinking
- Schema-driven data cleaning
- Row-level validation with rejection reasons
- Multi-table joins with Pandas
- Aggregations with `groupby()`
- Production-style logging