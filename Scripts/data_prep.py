# scripts/data_scrubber.py

import pandas as pd

class DataScrubber:
    """Reusable class for cleaning and preparing data."""

    def remove_duplicates(self, df):
        """Remove duplicate rows."""
        return df.drop_duplicates()

    def handle_missing_values(self, df, strategy='drop', fill_value=None):
        """
        Handle missing values in the dataframe.
        strategy: 'drop' or 'fill'
        fill_value: value to use if filling
        """
        if strategy == 'drop':
            return df.dropna()
        elif strategy == 'fill':
            return df.fillna(fill_value)
        else:
            raise ValueError("Invalid strategy. Use 'drop' or 'fill'.")

    def standardize_column_names(self, df):
        """Standardize column names by making them lowercase and replacing spaces with underscores."""
        df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
        return df

    def convert_dates(self, df, date_columns):
        """Convert specified columns to datetime format."""
        for col in date_columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')
        return df

    def trim_whitespace(self, df):
        """Trim leading/trailing whitespace from string columns."""
        for col in df.select_dtypes(include='object').columns:
            df[col] = df[col].str.strip()
        return df
