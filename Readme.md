<!-- # E-commerce Data Project

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
``` -->


# E-commerce Data Project

## Overview
An end-to-end pipeline for e-commerce sales data analysis, modeling, and visualization.

## Structure

- `etl/`: Extract, transform, and load data.
- `models/`: EDA and machine learning scripts.
- `app/`: Streamlit-based dashboard.

## Main Logic
The main logic for exploratory data analysis (EDA) and data processing can be found in the `models/eda.ipynb` file. This file contains the steps for analyzing the e-commerce sales data, cleaning the data, and preparing it for visualization.

## Usage

### Prerequisites

Make sure you have the following installed:

- **Docker** (for containerized setup)
- **Python 3.x** (if running locally without Docker)
- **PostgreSQL** (for the database)

### Running with Docker Compose

1. Clone the repository:

```bash
git clone https://github.com/yourusername/ecommerce-dashboard.git
cd ecommerce-dashboard
```

2. Navigate to the docker directory and run:

```bash
docker compose -p ecommerce up -d
```

3. Visit the Streamlit app at:
```bash
http://localhost:8501
```

### Running Locally

1. Clone the repository:

```bash
git clone https://github.com/GalkaKG/E-Commerce-Sales.git
cd ecommerce-dashboard
```

2. Create a virtual environment and activate it:

```bash
python3 -m venv env
\env\Scripts\Activate.ps1  # for Windows
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Set up your PostgreSQL database with the appropriate data.

5. Run the Streamlit app locally:

```bash
streamlit run app.py
```
