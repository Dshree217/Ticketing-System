class CommandConstants:
    CREATE_PARKING_LOT = "Create_parking_lot"
    DO_PARK = "Park"
    SLOT_NUMBERS_FOR_DRIVER_OF_AGE = "Slot_numbers_for_driver_of_age"
    SLOT_NUMBER_FOR_CAR_WITH_NUMBER = "Slot_number_for_car_with_number"
    DO_LEAVE = "Leave"
    VEHICLE_REGISTRATION_NUMBER_FOR_DRIVER_OF_AGE = "Vehicle_registration_number_for_driver_of_age"


class OutputMessage:
    SLOT_CREATED_MESSAGE = "Created parking of {} slots"
    PARKING_SPOT_SET_MESSAGE = "Car with vehicle registration number {} has been parked at slot number {}"
    SLOT_VACATED_MESSAGE = "Slot number {} vacated, the car with vehicle " \
                           "registration number {} left the space, the driver of the car was of age {}"
    NO_VACANT_PARKING_SLOT = "No parking slot is vacant. Please try again later"
    INVALID_PARKING_SLOT = "Invalid parking slot"
    PARKING_SLOT_ALREADY_VACANT = "Parking spot already vacant"
    NO_SLOTS_FOUND = "No slots found"
    NO_VEHICLES_FOUND = "No vehicles found"
    VEHICLE_ALREADY_IN_SLOT = "Vehicle with car number {} already parked"
