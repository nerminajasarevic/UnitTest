import unittest
from datetime import datetime

class UnitTest(unittest.TestCase):

    def test_symbol(self):
        symbol = 'SYMBOL'
        
        self.assertTrue(symbol.isalpha() and 1 <= len(symbol) <= 7 and symbol.isupper())

    def test_chart(self):
        for i in '12':
            self.assertIn(i, ['1', '2'])

    def test_time_series(self):
        for i in '1234':
            self.assertIn(i, ['1', '2', '3', '4'])

    #should work for start and end date
    def test_date(self):
        valid_dates = ['2020-01-01', '2024-01-01']
        for date in valid_dates:
            datetime.strptime(date, '%Y-%m-%d')

if __name__ == "__main__":
    unittest.main()
