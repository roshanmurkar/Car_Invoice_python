import pytest

from main import InvoiceGenerator, NegativeValueError,InvalidNumericData,UserInfo,RideDetails


class TestCalculator:

    def test_single_ride(self):
        assert InvoiceGenerator(1,10,20).calculate_fare_normal_ride() == (1, 10, 20, 125, 'normal')
        assert InvoiceGenerator(1,10,20).calculate_fare_premium_ride() == (1, 10, 20, 200, 'premium')

    def test_minimum_fare(self):
        assert InvoiceGenerator(1,0.6,1).calculate_fare_normal_ride() == (1, 0.6, 1, 5, 'normal')
        assert InvoiceGenerator(1,0.5, 1).calculate_fare_premium_ride() == (1, 0.5, 1, 10,'premium')

    def test_multiple_rides(self):
        ride1 = InvoiceGenerator(1,20,60).calculate_fare_normal_ride()
        ride2 = InvoiceGenerator(1,10,20).calculate_fare_normal_ride()
        InvoiceGenerator.ride_list.append(ride1)
        InvoiceGenerator.ride_list.append(ride2)
        assert RideDetails.calculate_total_fare() == 390

    def test_exceptions(self):
        with pytest.raises(NegativeValueError):
            assert InvoiceGenerator(1,-10,10).calculate_fare_normal_ride()

    def test_raises(self):
        with pytest.raises(NegativeValueError) as execinfo:
            InvoiceGenerator(1,-10,10).calculate_fare_normal_ride()
        assert execinfo.value.args[0] == 'negative input'

    def test_user_data_by_id(self):
        ride1 = InvoiceGenerator(1, 20, 60).calculate_fare_normal_ride()
        ride2 = InvoiceGenerator(1, 10, 20).calculate_fare_normal_ride()
        InvoiceGenerator.ride_list.append(ride1)
        InvoiceGenerator.ride_list.append(ride2)
        assert UserInfo(1).get_data_by_user_id() == [(1, 20, 60, 265), (1, 10, 20, 125)]

    def test_total_rides_data(self):
        ride1 = InvoiceGenerator(1, 20, 40).calculate_fare_normal_ride()
        ride2 = InvoiceGenerator(2, 30, 60).calculate_fare_normal_ride()
        ride3 = InvoiceGenerator(3, 40, 80).calculate_fare_normal_ride()
        InvoiceGenerator.ride_list.append(ride1)
        InvoiceGenerator.ride_list.append(ride2)
        InvoiceGenerator.ride_list.append(ride3)
        assert RideDetails.calculate_total_fare() == 1095
