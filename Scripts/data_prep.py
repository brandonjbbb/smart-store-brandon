# scripts/data_prep.py

import os
import sys
import importlib.util
import pandas as pd

# Dynamically load logger.py from utils folder
logger_path = os.path.join(os.path.dirname(__file__), '..', 'utils', 'logger.py')
spec = importlib.util.spec_from_file_location("logger", logger_path)
logger_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(logger_module)
setup_logger = logger_module.setup_logger

# Set up logging
logger = setup_logger()

def main():
    logger.info("Starting data preparation...")

    try:
        # Load data from CSVs
        customers = pd.read_csv('Data/Raw/customers_data.csv')
        products = pd.read_csv('Data/Raw/Products_Data.csv')
        sales = pd.read_csv('Data/Raw/Sales_Data.csv')
    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")
        return

    # Log the dataset shapes
    logger.info(f"Customers Data Shape: {customers.shape}")
    logger.info(f"Products Data Shape: {products.shape}")
    logger.info(f"Sales Data Shape: {sales.shape}")

    logger.info("Data preparation completed.")

if __name__ == "__main__":
    main()
