
class RideDetails:
    def __init__(self,ride_details):
        self.total_kilometer = ride_details.get("total_kilometer")
        self.total_time = ride_details.get("total_time")
        self.total_fare = ride_details.get("total_fare")

    def __str__(self):
        return f"total_kilometer of ride is = {self.total_kilometer}\n"\
               f"total_time of ride is = {self.total_time}\n"\
               f"total_fare of ride is = {self.total_fare}\n"


class InvoiceGenerator:
    def __init__(self):
        self.ride_list = []

    def calculate_fare(self,total_kilometer,total_time):
        """
        This function calculate total fare of single ride.
        :param total_kilometer: getting value from user
        :param total_time: getting value from user
        :return: dictionary that contains total_kilometer,total_time and total_fare
        """
        COST_PER_KM = 10
        COST_PER_MINUTE = 1
        MINIMUM_FARE = 5
        #total_kilometer = input("Enter total kilometer of ride :\t")
        #total_time = input("Enter total time of ride :\t")
        if float(total_kilometer) < 1:
            total_fare = MINIMUM_FARE
        else:
            total_fare = ((int(total_kilometer) * int(COST_PER_KM)) + (int(total_time) * int(COST_PER_MINUTE)) + int(MINIMUM_FARE))
        ride_dict = {
            "total_kilometer": total_kilometer,
            "total_time": total_time,
            "total_fare": total_fare
        }
        self.ride_list.append(total_fare)
        ride_details = RideDetails(ride_dict)
        return ride_details

    def calculate_avg_fare(self):
        length = len(self.ride_list)
        sum_of_total_fare = sum(self.ride_list)
        avg_fare = sum_of_total_fare/length
        print(f"Total number of rides is -> {length}")
        print(f"Total fare of all rides is -> {sum_of_total_fare}")
        print(f"Average fare of all rides is -> {avg_fare}")

if __name__ == '__main__':
    check = InvoiceGenerator()
    ride1 = check.calculate_fare(10,20)
    ride2 = check.calculate_fare(20, 40)
    ride3 = check.calculate_fare(30,60)
    ride4 = check.calculate_fare(40,80)
    #print(ride1.__str__())
    #print(ride2.__str__())
    #print(ride3.__str__())
    #print(ride4.__str__())
    check.calculate_avg_fare()