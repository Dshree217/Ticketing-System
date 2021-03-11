from collections import deque
from ticket import Ticket
from constants import OutputMessage as output_messages


class TicketManager:

    def __init__(self, n):
        """
        To create parking slots and maintain a list of free and filled parking slots
        :param n: number of parking slots to be created
        """
        self.number_of_spots = int(n)
        self.parking_spots = [None for i in range(n)]
        self.filled_spots = set()
        self.empty_spots = deque(range(n-1, -1, -1))
        print(output_messages.SLOT_CREATED_MESSAGE.format(self.number_of_spots))

    def set_park_slot(self, car_number, age):
        """
        To find an empty parking spot and create the ticket for the same
        :param car_number: car registration number
        :param age: age of the driver
        :return: output string
        """
        if len(self.filled_spots) == self.number_of_spots:
            return output_messages.NO_VACANT_PARKING_SLOT
        elif self.get_slot_number_by_car_number(car_number) == output_messages.NO_SLOTS_FOUND:
            spot = self.empty_spots.pop()
            self.parking_spots[spot] = Ticket(age, car_number)
            self.filled_spots.add(spot)
            return output_messages.PARKING_SPOT_SET_MESSAGE.format(car_number, spot+1)
        else:
            return output_messages.VEHICLE_ALREADY_IN_SLOT.format(car_number)

    def vacate_park_slot(self, slot_number):
        """
        To set the parking slot as free when a car leaves
        :param slot_number: the slot number that is vacated
        :return: output string
        """
        spot = slot_number - 1
        if spot in self.filled_spots:
            parked_car_number = self.parking_spots[spot].get_car_number()
            parked_age = self.parking_spots[spot].get_age()
            self.parking_spots[spot] = None
            self.filled_spots.remove(spot)
            self.empty_spots.append(spot)
            return output_messages.SLOT_VACATED_MESSAGE.format(spot+1, parked_car_number, parked_age)
        else:
            if spot > self.number_of_spots:
                return output_messages.INVALID_PARKING_SLOT
            else:
                return output_messages.PARKING_SLOT_ALREADY_VACANT

    def get_slot_number_by_age(self, age):
        """
        To get the slot numbers where drivers of given age have parked
        :param age: age of the driver
        :return: list of slots where drivers of the requested age are parked
        """
        res = []
        for i in self.filled_spots:
            if self.parking_spots[i].get_age() == age:
                res.append(str(i + 1))
        if len(res) == 0:
            return output_messages.NO_SLOTS_FOUND
        return ", ".join(res)

    def get_slot_number_by_car_number(self, car_number):
        """
        To get the slots where given car numbers are parked
        :param car_number: registration number of the car
        :return: list of slots where the car is parked
        """
        res = []
        for i in self.filled_spots:
            if self.parking_spots[i].get_car_number() == car_number:
                return i + 1
        if len(res) == 0:
            return output_messages.NO_SLOTS_FOUND

    def get_car_number_by_age(self, age):
        """
        To get the car number of drivers of certain age
        :param age: age of the driver
        :return: list of car numbers whose drivers are of certain age
        """
        res = []
        for i in self.filled_spots:
            if self.parking_spots[i].get_age() == age:
                res.append(self.parking_spots[i].car_number)
        if len(res) == 0:
            return output_messages.NO_VEHICLES_FOUND
        return ", ".join(res)
