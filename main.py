import logging

logging.basicConfig(filename="car_invoice.log", filemode="w")
log = logging.getLogger()

class NegativeValueError(Exception):...
    #Raised when any value of given field is negative

class UserInfo:
    def __init__(self):
        self.user_ride_list = []

    def get_data_by_user_id(self,id_user):
        rides_list = InvoiceGenerator.ride_list
        #print(rides_list)
        for single_ride in rides_list:
            if id_user == single_ride['user_id']:
                self.user_ride_list.append(single_ride)
        print(self.user_ride_list)
        print(f"Data for user id -> {id_user}")
        print(f"total rides are -> {self.calculate_total_rides_user()}")
        print(f"total kilometers are -> {self.calculate_total_kilometer_user()}")
        print(f"total time is -> {self.calculate_total_time_user()}")
        print(f"total fare is -> {self.calculate_total_fare_user()}")
        print(f"Average fare is -> {self.calculate_avg_fare_user()}\n")
        self.user_ride_list.clear()

    def calculate_total_fare_user(self):
        user_total_fare = 0
        for single_ride in self.user_ride_list:
            user_total_fare += int(single_ride['total_fare'])
        return user_total_fare

    def calculate_avg_fare_user(self):
        numerator = self.calculate_total_fare_user()
        denominator = self.calculate_total_rides_user()
        user_avg_fare = numerator/denominator
        return user_avg_fare

    def calculate_total_kilometer_user(self):
        user_total_kilometer = 0
        for single_ride in self.user_ride_list:
            user_total_kilometer += int(single_ride['total_kilometer'])
        return user_total_kilometer

    def calculate_total_time_user(self):
        user_total_time = 0
        for single_ride in self.user_ride_list:
            user_total_time += int(single_ride['total_time'])
        return user_total_time

    def calculate_total_rides_user(self):
        user_total_rides = 0
        for single_ride in self.user_ride_list:
            user_total_rides += 1
        return user_total_rides



class RideDetails:

    @staticmethod
    def display_info():
        print(f"Total number of rides is -> {RideDetails.calculate_total_rides_user()}")
        print(f"Total kilometer of all rides -> {RideDetails.calculate_total_kilometers()}")
        print(f"Total time of all rides -> {RideDetails.calculate_total_time()}")
        print(f"Total fare of all rides is -> {RideDetails.calculate_total_fare()}")
        print(f"Average fare of all rides is -> {RideDetails.avg_fare()}")

    @staticmethod
    def avg_fare():
        numerator = RideDetails.calculate_total_fare()
        denominator = RideDetails.calculate_total_rides_user()
        avg_fare = numerator/denominator
        return avg_fare

    @staticmethod
    def calculate_total_rides_user():
        rides_list = InvoiceGenerator.ride_list
        final_total_rides = 0
        for rides in rides_list:
            final_total_rides += 1
        return final_total_rides

    @staticmethod
    def calculate_total_kilometers():
        rides_list = InvoiceGenerator.ride_list
        final_total_kilometers = 0
        for rides in rides_list:
            final_total_kilometers += int(rides['total_kilometer'])
        return final_total_kilometers

    @staticmethod
    def calculate_total_time():
        rides_list = InvoiceGenerator.ride_list
        final_total_time = 0
        for rides in rides_list:
            final_total_time += int(rides['total_time'])
        return final_total_time

    @staticmethod
    def calculate_total_fare():
        rides_list = InvoiceGenerator.ride_list
        final_total_fare = 0
        for rides in rides_list:
            final_total_fare += int(rides['total_fare'])
        return final_total_fare


class InvoiceGenerator:
    ride_list = []

    def calculate_fare_normal_ride(self,u_id,total_kilometer,total_time):

        COST_PER_KM = 10
        COST_PER_MINUTE = 1
        MINIMUM_FARE = 5

        #try:
        if int(total_kilometer) < 0 or int(total_time) < 0:
            raise NegativeValueError("negative input")
        elif int(total_kilometer) < 1:
            total_fare = MINIMUM_FARE
        else:
            total_fare = ((int(total_kilometer) * int(COST_PER_KM)) + (int(total_time) * int(COST_PER_MINUTE)) + int(MINIMUM_FARE))
        #except NegativeValueError:
            #print("Entered value is negative")
            #log.warning("Values should be positive")
            #return None

        ride_dict = {
            "user_id": u_id,
            "total_kilometer": total_kilometer,
            "total_time": total_time,
            "total_fare": total_fare
        }
        details_list = self.ride_list.append(ride_dict)
        return details_list
        #ride_details = RideDetails(ride_dict)
        #return ride_details



if __name__ == '__main__':

    print("**********-> Welcome to Cab Invoice Generator <-**********")
    user_info = UserInfo()
    invoice = InvoiceGenerator()

    while True:
        user_choice = int(input("1-Normal Ride\n2-Premium Ride\n3-Invoice by User id \n4-Total Rides Details\n5-exit"))
        if user_choice == 1:
            user_id = input("Enter user id ")
            kilometer = input("Enter kilometer")
            time = input("Enter time")
            invoice.calculate_fare_normal_ride(user_id, kilometer, time)
        elif user_choice == 2:
            RideDetails.display_info()
            # user_id = input("Enter ui ")
            # km = input("Enter km")
            # tm = input("Enter tm")
            #a.calculate_fare_normal_ride(ui,km,tm)
        elif user_choice == 3:
            id = input("Enter user id")
            user_info.get_data_by_user_id(id)
        elif user_choice == 4:
            RideDetails.display_info()
        else:
            exit(0)
            print("enter valid value")




    # check = InvoiceGenerator()
    # ride1 = check.calculate_fare(-10,20)
    # ride2 = check.calculate_fare(20, 40)
    # ride3 = check.calculate_fare(30,60)
    # ride4 = check.calculate_fare(40,80)
    # print(ride1.__str__())
    # print(ride2.__str__())
    # print(ride3.__str__())
    # print(ride4.__str__())
    # check.calculate_avg_fare()