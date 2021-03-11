import sys

from constants import CommandConstants as cmd_constants
from ticket_manager import TicketManager


def process_input(commands):
    """
    To extract the commands from the input file and process the same
    :param commands: A list of commands to be executed
    :return:
    """
    ticket_manager = None
    create_command = commands[0].split(" ")
    if create_command[0] == cmd_constants.CREATE_PARKING_LOT:
        ticket_manager = TicketManager(int(create_command[1]))
    for command in commands[1:]:
        command = command.split(" ")
        if command[0] == cmd_constants.DO_PARK:
            print(ticket_manager.set_park_slot(car_number=command[1], age=command[3]))
        elif command[0] == cmd_constants.DO_LEAVE:
            print(ticket_manager.vacate_park_slot(slot_number=int(command[1])))
        elif command[0] == cmd_constants.SLOT_NUMBERS_FOR_DRIVER_OF_AGE:
            print(ticket_manager.get_slot_number_by_age(age=command[1]))
        elif command[0] == cmd_constants.SLOT_NUMBER_FOR_CAR_WITH_NUMBER:
            print(ticket_manager.get_slot_number_by_car_number(car_number=command[1]))
        elif command[0] == cmd_constants.VEHICLE_REGISTRATION_NUMBER_FOR_DRIVER_OF_AGE:
            print(ticket_manager.get_car_number_by_age(age=command[1]))


if __name__ == "__main__":
    file_name = ""
    commands = []
    if len(sys.argv) == 1:
        print("No file name given. Please enter file name: ")
        file_name = input()
    else:
        file_name = sys.argv[1]

    with open(file_name, 'r') as file:
        for line in file:
            commands.append(line.strip())

    process_input(commands)






