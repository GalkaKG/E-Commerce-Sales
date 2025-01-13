# E-commerce Data Project

## Overview
An end-to-end pipeline for e-commerce sales data analysis, modeling, and visualization.

## Structure
- `etl/`: Extract, transform, and load data.
- `models/`: EDA and machine learning scripts.
- `app/`: Streamlit-based dashboard.

## Usage
1. Run Docker Compose in docker directory: `docker compose -p ecommerce up -d`.
2. Visit Streamlit app at `http://localhost:8501`.

## More info
A full backup of the PostgreSQL database is available in the data folder. This backup includes the latest version of the ecommerce database, which contains the amazon_sales_report table and other relevant data.

To restore the database, you can use the following command:

```bash
pg_restore -U postgres -d ecommerce -1 /path/to/data/ecommerce_backup.dump
```