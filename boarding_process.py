import random

from passenger import Passenger


class BoardingProcess:
    def __init__(self, plane, passenger_list):
        self.plane = plane
        self.passenger_list = passenger_list

    def board(self):
        raise NotImplementedError()

    def assign_seats(self):
        raise NotImplementedError()


class SequentialBoarding(BoardingProcess):
    def assign_seats(self):
        pass

    def __str__(self):
        return 'Sequential Boarding Process'

    def board(self):
        if not self.plane or not self.passenger_list:
            raise Exception('Need a plane and passenger list to board')

        print('\nBoarding with {} '.format(self))

        for p in self.passenger_list:
            assert isinstance(p, Passenger)
            if not p.seat_number:
                raise Exception('Need a seat number')
            if not p.row_number:
                raise Exception('Need a row number')

            print('Passenger trying to get to Row {} Seat {}'.format(p.row_number, p.seat_number))


class RandomBoarding(BoardingProcess):

    def __str__(self):
        return 'Random Boarding Process'

    def board(self):

        if not self.plane or not self.passenger_list:
            raise Exception('Need a plane and passenger list to board')

        print('\nBoarding with {} '.format(self))

        self.assign_seats()

        for p in self.passenger_list:
            assert isinstance(p, Passenger)

            print(p)

            if p.seat_number is None:
                raise Exception('Need a seat number')
            if p.row_number is None:
                raise Exception('Need a row number')

            print('Passenger trying to get to Row {} Seat {}'.format(p.row_number, p.seat_number))

    def assign_seats(self):
        if not self.passenger_list:
            raise Exception('No passenger list to assign seats to.')

        seat_list = []
        for p in self.passenger_list:
            assert isinstance(p, Passenger)
            row = p.row_number = random.randint(0, self.plane.number_of_rows)
            seat = p.seat_number = random.randint(0, self.plane.seats_per_row)

            seat_list.append([row, seat])

    def print_seating_plan(self):
        for idx, p in enumerate(self.passenger_list):
            assert isinstance(p, Passenger)
            print('Passenger {} placed in row {}, seat {}.'.format(idx, p.row_number, p.seat_number))

