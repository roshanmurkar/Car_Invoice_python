
from main import InvoiceGenerator
#import unittest


class TestCalculator:
    def test_output(self):
        check = InvoiceGenerator.calculate_fare(20,60)
        assert check.total_fare == 265

    def test_null(self):
        check = InvoiceGenerator.calculate_fare(0.6,0)
        assert check.total_fare == 5