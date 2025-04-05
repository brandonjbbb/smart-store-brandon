import unittest
import pandas as pd
from scripts.data_scrubber import DataScrubber

class TestDataScrubber(unittest.TestCase):
    def setUp(self):
        self.scrubber = DataScrubber()
        self.df_with_duplicates = pd.DataFrame({
            'Name': ['Alice', 'Bob', 'Alice'],
            'Age': [25, 30, 25]
        })
        self.df_with_missing = pd.DataFrame({
            'Name': ['Alice', None, 'Charlie'],
            'Age': [25, 30, None]
        })
        self.df_with_dates = pd.DataFrame({
            'JoinDate': ['2020-01-01', 'not_a_date', '2022-06-15']
        })
        self.df_dirty_columns = pd.DataFrame({
            ' First Name ': ['Alice'],
            'Last Name': ['Smith']
        })
        self.df_with_spaces = pd.DataFrame({
            'City': [' New York ', ' Los Angeles ', ' Chicago ']
        })

    def test_remove_duplicates(self):
        cleaned = self.scrubber.remove_duplicates(self.df_with_duplicates)
        self.assertEqual(len(cleaned), 2)

    def test_handle_missing_values_drop(self):
        cleaned = self.scrubber.handle_missing_values(self.df_with_missing, strategy='drop')
        self.assertEqual(len(cleaned), 1)

    def test_handle_missing_values_fill(self):
        cleaned = self.scrubber.handle_missing_values(self.df_with_missing, strategy='fill', fill_value='Unknown')
        self.assertTrue(cleaned.isnull().sum().sum() == 0)

    def test_standardize_column_names(self):
        cleaned = self.scrubber.standardize_column_names(self.df_dirty_columns)
        self.assertIn('first_name', cleaned.columns)
        self.assertIn('last_name', cleaned.columns)

    def test_convert_dates(self):
        cleaned = self.scrubber.convert_dates(self.df_with_dates, ['JoinDate'])
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(cleaned['JoinDate']))

    def test_trim_whitespace(self):
        cleaned = self.scrubber.trim_whitespace(self.df_with_spaces)
        self.assertListEqual(cleaned['City'].tolist(), ['New York', 'Los Angeles', 'Chicago'])

if __name__ == '__main__':
    unittest.main()
