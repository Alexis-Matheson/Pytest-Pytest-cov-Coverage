#Test_LeapYear.py

import unittest
import LeapYearErrorHandling

class Year(unittest.TestCase):
    def test_calc(self):
        self.assertEqual(LeapYearErrorHandling.calc(2000), True)
        self.assertEqual(LeapYearErrorHandling.calc(1995), False)
       # self.assertEqual(LeapYearErrorHandling.calc(2000), False)

if __name__ == "__main__":
    unittest.main(verbosity=2)