import pytest

from main import InvoiceGenerator, NegativeValueError


class TestCalculator:
    def test_output(self):
        check = InvoiceGenerator.calculate_fare(0,20,60)
        assert check.total_fare == 265

    def test_null(self):
        check = InvoiceGenerator.calculate_fare(0,0.6,0)
        assert check.total_fare == 5

    def test_exceptions(self):
        with pytest.raises(NegativeValueError):
            assert InvoiceGenerator.calculate_fare(0,-10,10)

    def test_raises(self):
        with pytest.raises(NegativeValueError) as execinfo:
            InvoiceGenerator.calculate_fare(0, -10, 10)
        # these asserts are identical; you can use either one
        assert execinfo.value.args[0] == 'negative input'
        #assert str(execinfo.value) == 'some info'