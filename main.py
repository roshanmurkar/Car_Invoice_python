import logging

logging.basicConfig(filename="car_invoice.log", filemode="w")
log = logging.getLogger()

class NegativeValueError(Exception):...
    #Raised when any value of given field is negative

class InvalidNumericData(Exception):...
    #Raise when any value of given field is not numeric

class UserInfo:
    def __init__(self,id_user):
        self.user_ride_list = []
        self.id_user = id_user

    def get_data_by_user_id(self):
        """
        In this function we perform operation for getting all details of  single user
        :return: total info of single user rides
        """
        rides_list = InvoiceGenerator.ride_list
        self.user_ride_list.clear()
        #print(rides_list)
        for single_ride in rides_list:
            if self.id_user == single_ride[0]:
                self.user_ride_list.append(single_ride)
        self.display_user_data()
        return self.user_ride_list

    def display_user_data(self):
        print(f"Invoice for user id -> {self.id_user}")
        print(f"total rides are -> {self.calculate_total_rides_user()}")
        print(f"total kilometers are -> {self.calculate_total_kilometer_user()}")
        print(f"total time is -> {self.calculate_total_time_user()}")
        print(f"total fare is -> {self.calculate_total_fare_user()}")
        print(f"Average fare is -> {self.calculate_avg_fare_user()}\n")



    def calculate_total_fare_user(self):
        user_total_fare = 0
        for single_ride in self.user_ride_list:
            user_total_fare += int(single_ride[3])
        return user_total_fare

    def calculate_avg_fare_user(self):
        numerator = self.calculate_total_fare_user()
        denominator = self.calculate_total_rides_user()
        user_avg_fare = numerator/denominator
        return user_avg_fare

    def calculate_total_kilometer_user(self):
        user_total_kilometer = 0
        for single_ride in self.user_ride_list:
            user_total_kilometer += int(single_ride[1])
        return user_total_kilometer

    def calculate_total_time_user(self):
        user_total_time = 0
        for single_ride in self.user_ride_list:
            user_total_time += int(single_ride[2])
        return user_total_time

    def calculate_total_rides_user(self):
        user_total_rides = 0
        for single_ride in self.user_ride_list:
            user_total_rides += 1
        return user_total_rides



class RideDetails:

    @staticmethod
    def display_info():
        """
        This function for displaying all data
        :return: Total and Average of all rides
        """
        print(f"Total number of rides is -> {RideDetails.calculate_total_rides_user()}")
        print(f"Total kilometer of all rides -> {RideDetails.calculate_total_kilometers()}")
        print(f"Total time of all rides -> {RideDetails.calculate_total_time()}")
        print(f"Total fare of all rides is -> {RideDetails.calculate_total_fare()}")
        print(f"Average fare of all rides is -> {RideDetails.avg_fare()}")

    @staticmethod
    def avg_fare():
        """
        In this function we calculating average fare of all rides that present in ride_list
        :return: average fare of all rides
        """
        numerator = RideDetails.calculate_total_fare()
        denominator = RideDetails.calculate_total_rides_user()
        avg_fare = numerator/denominator
        return avg_fare

    @staticmethod
    def calculate_total_rides_user():
        """
        in this function we calculating total rides
        :return: total number of rides
        """
        rides_list = InvoiceGenerator.ride_list
        final_total_rides = 0
        for rides in rides_list:
            final_total_rides += 1
        return final_total_rides

    @staticmethod
    def calculate_total_kilometers():
        """
        In this function we calculating sum of all rides kilometers
        :return: total kilometer
        """
        rides_list = InvoiceGenerator.ride_list
        final_total_kilometers = 0
        for rides in rides_list:
            final_total_kilometers += int(rides[1])
        return final_total_kilometers

    @staticmethod
    def calculate_total_time():
        """
        In this function we calculating sum of all rides time
        :return: total time
        """
        rides_list = InvoiceGenerator.ride_list
        final_total_time = 0
        for rides in rides_list:
            final_total_time += int(rides[2])
        return final_total_time

    @staticmethod
    def calculate_total_fare():
        """
        In this function we calculating sum of all rides fare
        :return: total fare
        """
        rides_list = InvoiceGenerator.ride_list
        final_total_fare = 0
        for rides in rides_list:
            final_total_fare += int(rides[3])
        return final_total_fare


class InvoiceGenerator:
    ride_list = []

    def __init__(self,user_id, total_kilometer, total_time):
        self.user_id = user_id
        self.total_kilometer = total_kilometer
        self.total_time = total_time

    def calculate_fare_normal_ride(self):
        """
        In this function we calculating total fare of single ride and
        storing values in a list in the form of dictionary.
        :return: ride_list that contains all rides in the form of dictionary
        """
        COST_PER_KM = 10
        COST_PER_MINUTE = 1
        MINIMUM_FARE = 5
        mode = "normal"
        #try:
        if int(self.total_kilometer) < 0 or int(self.total_time) < 0:
            raise NegativeValueError("negative input")
        elif int(self.total_kilometer) < 1:
            total_fare = MINIMUM_FARE
        else:
            total_fare = ((int(self.total_kilometer) * int(COST_PER_KM)) + (int(self.total_time) * int(COST_PER_MINUTE)) + int(MINIMUM_FARE))
        #except NegativeValueError:
            #print("Entered value is negative")
            #log.warning("Values should be positive")
            #return None
        return self.user_id,self.total_kilometer,self.total_time,total_fare,mode

    def calculate_fare_premium_ride(self):
        """
        In this function we calculating total fare of single ride and
        storing values in a list in the form of dictionary.
        :return: ride_list that contains all rides in the form of dictionary
        """
        COST_PER_KM = 15
        COST_PER_MINUTE = 2
        MINIMUM_FARE = 10
        mode = "premium"
        #try:
        if int(self.total_kilometer) < 0 or int(self.total_time) < 0:
            raise NegativeValueError("negative input")
        elif int(self.total_kilometer) < 1:
            total_fare = MINIMUM_FARE
        else:
            total_fare = ((int(self.total_kilometer) * int(COST_PER_KM)) + (int(self.total_time) * int(COST_PER_MINUTE)) + int(MINIMUM_FARE))
        #except NegativeValueError:
            #print("Entered value is negative")
            #log.warning("Values should be positive")
            #return None
        return self.user_id,self.total_kilometer,self.total_time,total_fare,mode

    @staticmethod
    def display_data():
        for obj in InvoiceGenerator.ride_list:
            print(obj)

    @staticmethod
    def get_user_id():
        """
        Taking input from user for user_id
        :return: user id for further calculation
        """
        try:
            u_id = input("Enter user id ")
            if not u_id.isnumeric():
                raise InvalidNumericData
        except InvalidNumericData:
            print("Enter numeric data")
            log.warning("Enter numeric data")
            return None
        return u_id

    @staticmethod
    def get_kilometer():
        """
        Taking input from user for kilometer
        :return: kilometer for further calculation
        """
        try:
            input_kilometer = input("Enter kilometer")
            if not input_kilometer.isnumeric():
                raise InvalidNumericData
        except InvalidNumericData:
            print("Enter numeric data")
            log.warning("Enter numeric data")
            return None
        return input_kilometer

    @staticmethod
    def get_time():
        """
        Taking input from user for time
        :return: time for further calculation
        """
        try:
            input_time = input("Enter time")
            if not input_time.isnumeric():
                raise InvalidNumericData
        except InvalidNumericData:
            print("Enter numeric data")
            log.warning("Enter numeric data")
            return None
        return input_time
if __name__ == '__main__':

    print("**********-> Welcome to Cab Invoice Generator <-**********")
    while True:
        user_choice = int(input("1-Normal Ride\n2-Premium Ride\n3-Invoice by User id \n4-Total Rides Details\n5-exit"))
        if user_choice == 1:
            u_id = InvoiceGenerator.get_user_id()
            kilometer = InvoiceGenerator.get_kilometer()
            time = InvoiceGenerator.get_time()
            invoice_object = InvoiceGenerator(u_id,kilometer,time).calculate_fare_normal_ride()
            InvoiceGenerator.ride_list.append(invoice_object)
            InvoiceGenerator.display_data()
        elif user_choice == 2:
            u_id = InvoiceGenerator.get_user_id()
            kilometer = InvoiceGenerator.get_kilometer()
            time = InvoiceGenerator.get_time()
            invoice_object = InvoiceGenerator(u_id, kilometer, time).calculate_fare_premium_ride()
            InvoiceGenerator.ride_list.append(invoice_object)
            InvoiceGenerator.display_data()
        elif user_choice == 3:
            id = InvoiceGenerator.get_user_id()
            UserInfo(id).get_data_by_user_id()
        elif user_choice == 4:
            RideDetails.display_info()
        else:
            exit(0)
            print("enter valid value")
