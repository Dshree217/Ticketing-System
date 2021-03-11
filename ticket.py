class Ticket:

    def __init__(self, age, car_number):
        self.age = age
        self.car_number = car_number

    def get_age(self):
        """
        To get the age of driver of a ticket
        :return: age of the driver
        """
        return self.age

    def get_car_number(self):
        """
        To get the car number of the ticket
        :return: car number
        """
        return self.car_number


